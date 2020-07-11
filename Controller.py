import web
from Models import RegisterModel,LoginModel,Posts

web.config.debug = False

urls= (
    '/','Home',
    '/register','Register',
    '/login', 'Login',
    '/logout','Logout',
    '/postregistration','PostRegistration',
    '/check-login', 'CheckLogin',
    '/discover','Discover',
    '/profile','Profile',
    '/settings','Settings',
    '/post-activity','PostActivity'


)

app=web.application(urls,globals())
session=web.session.Session(app,web.session.DiskStore("sessions"),initializer={"user": None})
session_data = session._initializer

render=web.template.render("Views/Templates", base="MainLayout",globals={"session":session_data,"current_user": session_data["user"]})

class Home:
    def GET(self):
        data=type('obj',(object,),{"username":"jainshreya1808","password":"Shreya"})
        login=LoginModel.LoginModel()
        isCorrect=login.check_user(data)

        if isCorrect:
            session_data["user"]=isCorrect

        post_model=Posts.Posts()
        posts=post_model.get_all_post()

        return render.home(posts)

class Login:
    def GET(self):
        return render.login()

class Register:
    def GET(self):
        return render.register()

class Discover:
    def GET(self):
        return render.discover()

class Profile:
    def GET(self):
        return render.profile()

class Settings:
    def GET(self):
        return render.settings()

class PostRegistration:
    def POST(self):
        data = web.input()
        reg_model=RegisterModel.RegisterModel()
        reg_model.insert_user(data)
        return data.first_name

class CheckLogin:
    def POST(self):
        data = web.input()
        login = LoginModel.LoginModel()
        isCorrect = login.check_user(data)

        if isCorrect:
            session_data["user"]=isCorrect
            return isCorrect

        return "error"

class Logout:
    def GET(self):
        session["user"]= None
        session_data["user"]= None
        session.kill()
        return "success"
class PostActivity:
    def POST(self):
        data=web.input()
        data.username=session_data['user']["username"]

        post_model= Posts.Posts()
        post_model.insert_post(data)
        return "success"



if __name__=="__main__":
    app.run()