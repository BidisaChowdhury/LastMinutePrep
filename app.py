from flask import Flask,render_template, request
from youtube_transcript_api import YouTubeTranscriptApi
import cohere
co = cohere.Client('s2AJODpOUgAjZmZ0z2wZcNm41pdhiLh2nchFjTy3')


app = Flask(__name__)


@app.route("/home")
def home():
    return render_template("index.html")
@app.route('/os',methods=['Post','GET'])
def summary_api():
    # output=request.form.to_dict()
    url1= "https://www.youtube.com/watch?v=26QPDBe-NB8&t=142s"
    #url2="https://www.youtube.com/watch?v=0u78hx-66Xk"
    video_id = url1.split('=')[1]
    summary = get_summary(get_transcript(video_id))
    # name=output[summary]
    return render_template('summary.html',summary=summary)

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
#coa
@app.route('/COA',methods=['Post','GET'])
def summary_api_2():
    # output=request.form.to_dict()
    #url= "https://www.youtube.com/watch?v=26QPDBe-NB8&t=142s"
    url2="https://www.youtube.com/watch?v=6_PHIL4LZEU"
    video_id2 = url2.split('=')[1]
    summary = get_summary(get_transcript(video_id2))
    # name=output[summary]
    return render_template('summary.html',summary=summary)

def get_transcript_2(video_id2):
    transcript_list2 = YouTubeTranscriptApi.get_transcript(video_id2)
    transcript2 = ' '.join([d['text'] for d in transcript_list2])
    return transcript2

def get_summary(transcript2):
    response = co.summarize( 
  text=transcript2,
  length='medium',
  format='paragraph',
  model='summarize-xlarge',
  additional_command='',
  temperature=0.9,
   ) 
    return response.summary

#DAA
@app.route('/DAA',methods=['Post','GET'])
def summary_api_3():
    # output=request.form.to_dict()
    #url= "https://www.youtube.com/watch?v=26QPDBe-NB8&t=142s"
    url3="https://www.youtube.com/watch?v=0u78hx-66Xk"
    video_id3 = url3.split('=')[1]
    summary = get_summary(get_transcript(video_id3))
    # name=output[summary]
    return render_template('summary.html',summary=summary)

def get_transcript_3(video_id3):
    transcript_list3 = YouTubeTranscriptApi.get_transcript(video_id3)
    transcript3 = ' '.join([d['text'] for d in transcript_list3])
    return transcript3

def get_summary(transcript3):
    response = co.summarize( 
  text=transcript3,
  length='medium',
  format='paragraph',
  model='summarize-xlarge',
  additional_command='',
  temperature=0.9,
   ) 
    return response.summary
#DE
@app.route('/DE',methods=['Post','GET'])
def summary_api_4():
    # output=request.form.to_dict()
    #url= "https://www.youtube.com/watch?v=26QPDBe-NB8&t=142s"
    url4="https://www.youtube.com/watch?v=qpGA3pDjvjI"
    video_id4 = url4.split('=')[1]
    summary = get_summary(get_transcript(video_id4))
    # name=output[summary]
    return render_template('summary.html',summary=summary)

def get_transcript_4(video_id4):
    transcript_list4 = YouTubeTranscriptApi.get_transcript(video_id4)
    transcript4 = ' '.join([d['text'] for d in transcript_list4])
    return transcript4

def get_summary(transcript4):
    response = co.summarize( 
  text=transcript4,
  length='medium',
  format='paragraph',
  model='summarize-xlarge',
  additional_command='',
  temperature=0.9,
   ) 
    return response.summary
#DBMS
@app.route('/DBMS',methods=['Post','GET'])
def summary_api_5():
    # output=request.form.to_dict()
    #url= "https://www.youtube.com/watch?v=26QPDBe-NB8&t=142s"
    url5="https://www.youtube.com/watch?v=UsBJ9l5tajA"
    video_id5 = url5.split('=')[1]
    summary = get_summary(get_transcript(video_id5))
    # name=output[summary]
    return render_template('summary.html',summary=summary)

def get_transcript_5(video_id5):
    transcript_list5 = YouTubeTranscriptApi.get_transcript(video_id5)
    transcript5 = ' '.join([d['text'] for d in transcript_list5])
    return transcript5

def get_summary(transcript5):
    response = co.summarize( 
  text=transcript5,
  length='medium',
  format='paragraph',
  model='summarize-xlarge',
  additional_command='',
  temperature=0.9,
   ) 
    return response.summary

if __name__ == '__main__':
    app.run(debug=True,port=5555)