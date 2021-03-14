import sys
import csv
import os
import tempfile

# Define download format for Youtube-dl
formt = '"bestvideo[ext=mp4][fps<=30][height<=1080][height>=470]"'
codec = 'libx264 -pix_fmt yuv444p -preset slow -r 30 -psy 0 -qp 0 -8x8dct 1 -me_method umh -x264-params bframes=0'

# Download to targetdir based on video ID, start, and end
def download(ID, start, end, targetdir):
    # tempfile
    ytdlout = os.path.join(tempfile.gettempdir(),ID+'.mp4')
    # target file
    out = os.path.join(targetdir,'_'.join([ID, start, end]))+'.avi'
    
    # if target does not exist
    if not os.path.isfile(out):
        # if tempfile does not already exist
        if not os.path.isfile(ytdlout):
            # Download the tempfile using Youtube-dl
            print('Downloading ' + ID + '...')
            print('youtube-dl --no-check-certificate --output ' + \
                  os.path.join(tempfile.gettempdir(),r'%(id)s.%(ext)s') + \
                  ' --format ' + formt + ' ' + ID)
            if sys.platform == "linux" or sys.platform == "linux2":
            	os.system(('youtube-dl --no-check-certificate --output ' + \
                  os.path.join(tempfile.gettempdir(),'%\(id\)s.%\(ext\)s') + \
                  ' --format ' + formt + ' ' + ID))
            else:
                os.system(('youtube-dl --no-check-certificate --output ' + \
                  os.path.join(tempfile.gettempdir(),r'%(id)s.%(ext)s') + \
                  ' --format ' + formt + ' ' + ID))
        
        # Cut the tempfile using FFmpeg
        print('Cutting ' + ID + ' from ' + start + ' to ' + end + '...')
        os.system('ffmpeg -hide_banner -i ' + ytdlout + ' -ss ' + start + \
                  ' -to ' +  end + ' -c:v ' + codec + ' ' + out)

def main():
    # video list file
    csvfile = (sys.argv[1]).replace('\r','')
    print('Downloading ' + csvfile)
    
    # define targetdir
    targetdir = os.path.join(os.path.split(csvfile)[0], os.path.splitext(csvfile)[0])
    print('To ' + targetdir)
    
    # make dirs
    if not os.path.exists(targetdir):
        os.makedirs(targetdir)
        
    # read video list
    with open(csvfile, "rU") as myFile:  
        reader = csv.reader(myFile)
        # for each video
        for row in reader:
            row = list(map(str.strip,row))
            row = [x.replace('\r','') for x in row]
            # Call download function
            download(row[0], row[1], row[2], targetdir)
            
    print('Done!')

if __name__ == '__main__':
    main()
