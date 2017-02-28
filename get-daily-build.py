import os, re, datetime
from subprocess import run

def find_daily_build():

    #indir = '\\\\BN-EHUA03\GM_Info30_MY18_Daily\GM_Info30_MY18_Daily'
    #pattern = r'-[1-9]{3}_simulation'
    indir = 'C:\\Users\\AW\\Downloads'
    flist = []

    #now = datetime.datetime.now()
    #ago = now-dt.timedelta(minutes=120)

    for root, dirs, filenames in os.walk(indir):
        for f in filenames:
            if (re.findall(r'-[1-9]{3}_simulation', f)):
                fullpath = os.path.join(root, f)
                st = os.stat(fullpath)
                mtime = datetime.datetime.fromtimestamp(st.st_mtime)
                #if mtime > ago:
                str_mtime = str(mtime)
                str_today = str(datetime.date.today())
                if str_today == str_mtime[:10]:
                    #print('%s modified %s' % (fullpath, mtime))
                    flist.append(fullpath)

    flist = sorted(flist, reverse=True)
    daily_build = flist[0]
    return daily_build

def get_daily_build(daily_build):
    extract_path = r'C:\Users\AW\Downloads'
    z_path = r'"C:\Program Files\7-Zip\7z.exe"'
    extract_cmd = z_path + ' x ' + daily_build + ' -o' + extract_path
    print(extract_cmd)
    #run(extract_cmd)
    #run(r'"C:\Program Files\7-Zip\7z.exe" x ' + r"C:\Users\AW\Downloads\rp-0.91.zip" + ' -o' + extract_path)

get_daily_build(find_daily_build())