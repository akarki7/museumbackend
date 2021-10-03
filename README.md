# Museum Backend

Backend for virtual museum

### Architecture Notes
------------------
* Backend is written in Python and uses Django as the server
* For Database the system uses Postgresql for both local testing and production
* The frontend communicates with the backend using REST architecture.

### Requirements
--------------------------

* docker
* docker-compose


### How to run 
--------------------------


```bash
make build
make migrate
make run
```

You can go to `localhost:8000` to access the backend application.


### Testing
--------------------------

You can run the entire test suite using:

```bash
make test
```

### API endpoint documentation
--------------------------

You can access the swagger documentation for api endpoints by going to ```/api/v1/schema/swagger-ui```

### Notes for the contributors
------------------------------
* To add any new feature please fork the repo and create a Pull Request with main
* If you find any bug please create a issue in the Github repo. For other security issue you can contact at `karkiaabishkar@gmail.com` or `spaudel.dev@gmail.com`