import os
class FileOrganization:
    def __init__(self):
        self.none = "none"
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        os.chdir(self.dir_path)
    # add implementation for multiple ignore
    def fileDelete(self):
        x = input('front to delete(-1 for all): ')
        y = input('back to delete(-1 for all): ')
        kkk = input('keywordto delete(-1 if none): ')
        z = input('fronts to ignore: ')
        w = input('backs to ignore: ')

        ownName = os.path.basename(__file__)
        count = 0
        for f in os.listdir():
            if ( f != ownName and f != "System Volume Information"):
                file_name, file_ext = os.path.splitext(f)
                dsHveKyWrd = kkk in file_name
                if((file_ext != w) and (file_name != z) and ((x == file_name) or ( y == file_ext) or dsHveKyWrd ) ):
                    os.remove(f)
                    
    def renameFiles(x,y,z,w,kkk):
        '''
        #x = input('new front(-1 for same): ')
        y = input('new back(-1 for same): ')
        z = input('fronts to ignore(-1 if all): ')
        w = input('backs to ignore(-1 if all): ')
        kkk = input('number of leading 0s(if blank 2): ')
        '''
        try:
            int(kkk)
            Num = int(kkk)
        except ValueError:
            Num = 2
        Num = int(Num)
        ownName = os.path.basename(__file__)
        count=0

        for f in os.listdir():
            if ( f != ownName and f != "System Volume Information" and f != "ProgramManager.py"):
                file_name, file_ext = os.path.splitext(f)
                if((file_ext != w or w == '-1') and (file_name != z or z == '-1')):
                    if(x == '-1'):
                        newName = file_name
                    else:
                        count += 1
                        newNum = str(count).zfill(Num)
                        newName = str(newNum) + x
                    if (y == '-1'):
                        newName += file_ext
                    else:
                        newName += "." + y
                        #f_title, f_course, f_num = file_name.split("-")
                    os.rename(f, newName)


