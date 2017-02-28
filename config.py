import os
ACCESS_TOKEN = '<<PAGE_ACCESS_TOKEN>>'
PAGE_ID = '1792892714369394'

BASE_YEAR = 2017
BASE_URL = 'http://www.juexam.org/newexam/'
FIELDS = ['lstFaculty','lstCourse','lstYearOfExam', 'lstYearOfStudy','lstSemester','lstNatureOfExam']
DEPARTMENT_FIELD = 'lstDepartmentShow'
VALIDATION_STRINGS = ['Roll Number', 'EXR']
EXCLUDES = {'lstCourse':['Certificate / Diploma / Advance Diploma','Undergraduate (Annual System)','Postgraduate (Annual System)'],
            'lstSemester':['3rd Semester','4th Semester','5th Semester','6th Semester','7th Semester','Final','3rd & 4th Sem.'],
            'lstFaculty':['Arts','Int.-disc. Stud.,Law & Mgmnt.','Science']}
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

#heroku config:set PATH=$PATH:vendor/phantomjs/bin
#heroku config:set PATH="/usr/local/bin:/usr/bin:/bin:/app/vendor/phantomjs/bin"
#heroku config:set LD_LIBRARY_PATH=/usr/local/lib:/usr/lib:/lib:/app/vendor/phantomjs/lib