import sys
import csv
import os
import tempfile

formt = '"bestvideo[ext=mp4][fps<=30][height<=1080][height>=470]"'
codec = 'libx264 -pix_fmt yuv444p -preset slow -r 30 -psy 0 -qp 0 -8x8dct 1 -me_method umh -x264-params bframes=0'

def download(ID, start, end, targetdir):
    ytdlout = os.path.join(tempfile.gettempdir(),ID+'.mp4')
    out = os.path.join(targetdir,'_'.join([ID, start, end]))+'.avi'
    
    if not os.path.isfile(out):
        if not os.path.isfile(ytdlout):
            print('Downloading ' + ID + '...')
            print('youtube-dl --no-check-certificate --output ' + \
                  os.path.join(tempfile.gettempdir(),'%\(id\)s.%\(ext\)s') + \
                  ' --format ' + formt + ' ' + ID)
            os.system('youtube-dl --no-check-certificate --output ' + \
                  os.path.join(tempfile.gettempdir(),'%\(id\)s.%\(ext\)s') + \
                  ' --format ' + formt + ' ' + ID)
        
        print('Cutting ' + ID + ' from ' + start + ' to ' + end + '...')
        os.system('ffmpeg -hide_banner -i ' + ytdlout + ' -ss ' + start + \
                  ' -to ' +  end + ' -c:v ' + codec + ' ' + out)

def main():
    csvfile = (sys.argv[1])
    print('Downloading ' + csvfile)
    
    targetdir = os.path.join(os.path.split(csvfile)[0], os.path.splitext(csvfile)[0])
    print('To ' + targetdir)
    
    if not os.path.exists(targetdir):
        os.makedirs(targetdir)
        
    with open(csvfile, "rU") as myFile:  
        reader = csv.reader(myFile)
        for row in reader:
            row = list(map(str.strip,row))
            download(row[0], row[1], row[2], targetdir)
            
    print('Done!')

if __name__ == '__main__':
    main()