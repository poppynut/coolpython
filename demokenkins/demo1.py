import jenkins


#server = jenkins.Jenkins('http://localhost:8080',
        # username='myuser', password='mypassword')


server = jenkins.Jenkins('http://localhost:8080')
version = server.get_version()
print version