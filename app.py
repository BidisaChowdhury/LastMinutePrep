from flask import Flask, render_template, request
from youtube_transcript_api import YouTubeTranscriptApi
import cohere

app = Flask(__name__)

co = cohere.Client('s2AJODpOUgAjZmZ0z2wZcNm41pdhiLh2nchFjTy3')

@app.route("/home")
def home():
    return render_template("index.html")

@app.route('/os', methods=['POST', 'GET'])
def summary_os():
    url1 = "https://www.youtube.com/watch?v=26QPDBe-NB8&t=142s"
    video_id = url1.split('=')[1]
    summary = get_summary(get_transcript(video_id))
    subject_name = "Operating Systems"
    topic_name = "Introduction to OS"
    return render_template('summary.html', summary=summary, subject_name=subject_name, topic_name=topic_name)

@app.route('/coa', methods=['POST', 'GET'])
def summary_coa():
    url2 = "https://www.youtube.com/watch?v=6_PHIL4LZEU"
    video_id = url2.split('=')[1]
    summary = get_summary(get_transcript(video_id))
    subject_name = "Computer Organization and Architecture"
    topic_name = "Basics of COA"
    return render_template('summary.html', summary=summary, subject_name=subject_name, topic_name=topic_name)

@app.route('/daa', methods=['POST', 'GET'])
def summary_daa():
    url3 = "https://www.youtube.com/watch?v=0u78hx-66Xk"
    video_id = url3.split('=')[1]
    summary = get_summary(get_transcript(video_id))
    subject_name = "Design and Analysis of Algorithms"
    topic_name = "Introduction to Algorithms"
    return render_template('summary.html', summary=summary, subject_name=subject_name, topic_name=topic_name)

@app.route('/de', methods=['POST', 'GET'])
def summary_de():
    url4 = "https://www.youtube.com/watch?v=qpGA3pDjvjI"
    video_id = url4.split('=')[1]
    summary = get_summary(get_transcript(video_id))
    subject_name = "Digital Electronics"
    topic_name = "Boolean Algebra"
    return render_template('summary.html', summary=summary, subject_name=subject_name, topic_name=topic_name)

@app.route('/dbms', methods=['POST', 'GET'])
def summary_dbms():
    url5 = "https://www.youtube.com/watch?v=UsBJ9l5tajA"
    video_id = url5.split('=')[1]
    summary = get_summary(get_transcript(video_id))
    subject_name = "Database Management Systems"
    topic_name = "Introduction to DBMS"
    return render_template('summary.html', summary=summary, subject_name=subject_name, topic_name=topic_name)

def get_transcript(video_id):
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    transcript = ' '.join([d['text'] for d in transcript_list])
    return transcript

def get_summary(transcript):
    response = co.summarize(
        text=transcript,
        length='medium',
        format='paragraph',
        model='summarize-xlarge',
        additional_command='',
        temperature=0.9,
    )
    return response.summary

if __name__ == '__main__':
    app.run(debug=True, port=5555)
