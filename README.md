# mini-feed-2
**Reference: https://testdriven.io/courses/auth-flask-react/react-and-docker/**

Basic code for starting a new project

Go to http://localhost:3007/ for the react app (Comment out the client section in docker-compose for faster build in case you are not using react)

For REST, go to:
http://localhost:5001/ping

For Flask admin, go to:
http://localhost:5001/admin/user/


# Workflow using VSCode (Highly recommend)
(install remote container extension)
- remote-containers: reopen in container
(That's it, you get auto complete, per function run test, everything)

# Workflow if you are not using VSCode
- Build and run: make run
- Create db and dummy data: make builddb
- Run worker: make worker
- Run test: make test

# Features
- A fan out way of creating timeline. Use demo.sh to test it out
