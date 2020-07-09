import web
from Models import RegisterModel,LoginModel

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
    '/settings','Settings'


)

app=web.application(urls,globals())
session=web.session.Session(app,web.session.DiskStore("sessions"),initializer={"user": "none"})
session_data = session._initializer

render=web.template.render("Views/Templates", base="MainLayout",globals={"session":session_data,"current_user": session_data["user"]})

class Home:
    def GET(self):
        return render.home()

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
        session.kill()
        return "success"


if __name__=="__main__":
    app.run()