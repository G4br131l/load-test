from locust import task, TaskSet


class Usuario(TaskSet):
    def id_GET(self):
        self.client.get("/usuario/2")
    
    def updatePassword_POST(self):
        self.client.post(
            "/usuario/updatePassword",
            json={
                "oldPassword" : "87654321",
                "newPassword" : "12345678"
            }
        )

class Login(TaskSet):
    @task
    def logoff_GET(self):
        self.client.get("/login/logoff")

    @task
    def POST(self):
        self.client.post(
            "/login",
            json={
                "email": "fernandogab@gmail.com",
                "senha": "12345678"
            }
        )


class Signup(TaskSet):
    def POST(self):
        self.client.post(
            "/signup",
            json={
                "nome": "gabriel fernando",
                "email": "fernandogabril@gmail.com",
            }
        )


class Tags(TaskSet):
    def GET(self):
        self.client.get("/tags")


class Post(TaskSet):
    def query_GET(self):
        self.client.get("/post/?start=0&offset=0")

    def id_GET(self):
        self.client.get("/post/1")


class Image(TaskSet):
    def GET(self):
        self.client.get("/image/imagem")

    def POST(self):
        # multipart/form-data
        self.client.post("/image")


class DeleteUser(TaskSet):
    def GET(self):
        self.client.get("/delete-user/id")


class user_composto(TaskSet):
    login = Login

    @task
    def fun(self):
        self.login.POST(self)


class User_entra_e_sai(TaskSet):
    def on_start(self):
        self.client.post(
            "/login",
            json={
                "email": "fernandogab@gmail.com",
                "senha": "12345678"
            }
        )

    @task
    def id_GET(self):
        self.client.get("/usuario/2")
    
    @task
    def query_GET(self):
        self.client.get("/post/?start=0&offset=0")

    @task
    def id_GET(self):
        self.client.get("/post/1")
