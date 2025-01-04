pipeline{
    agent any
    stages{
        stage('STAGE 1 : Clone Repository'){
            steps{
                // clone the GitHub repository on the "main" branch
                git branch:'main', url:'https://github.com/sgangopadhyay/Testing-REST-API-Server-'
            }
        }
        stage('STAGE 2 : Install Dependencies'){
            steps{
                // install the python dependecies for the project
                bat 'pip install -r requirements.txt'
            }
        }
        stage('STAGE 3 : Run Python Unit Tests'){
            steps{
                // run the python unittest for the project
                bat 'python -m unittest -v testRestAPI.py'
            }
        }
    }
    post{
        always{
            // notify completion of the pipeline
            echo 'Pipeline Execution Completed'
        }
        failure{
            // log the failure for debugging
            echo 'Pipeline failed ! Check the logs for more details'
        }
        success{
            // log the success message
            echo 'Pipeline executed successfully !'
        }
    }

}
