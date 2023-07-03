from flask import Flask, render_template
# from tkinter import *
import speedtest 


# sp = Tk()
# dont need this, just use html




placeholder = '-'

speedtester = Flask(__name__)

@speedtester.route('/speedrun')
def speedcheeck():
    sp  = speedtest.Speedtest()
    sp.get_servers()
    downspeedd= str(round(sp.download() / (10**6),3))+" Mbs"
    upspeedd = str(round(sp.upload() / (10**6),3))+" Mbs"
    # ping = str(round(sp.get_best_server()/ (10**6),3))+" M/s"
    
    return render_template('index.html', uploadspeed = upspeedd, downloadspeed = downspeedd)
    # get best server may be a ping function
    # set the things in our html. 






@speedtester.route('/')
def index ():
    return render_template('index.html', uploadspeed=placeholder, downloadspeed =placeholder)
    # return "hello world"

# tkinters class

# sp.mainloop
# 




if __name__ == "__main__":
    speedtester.run(debug=True)