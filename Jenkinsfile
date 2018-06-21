pipeline {

    agent any
    stages {
        stage('Stage 1') {
            steps {
                echo 'Stage 1'
            }
        }
        
        stage('Stage 2') {
            steps {
                echo 'Stage 2'
                behave -f allure_behave.formatter:AllureFormatter -o allure-results features/scenarios/login.feature -D browser=chrome -D env=UAT
            }
        }
    }
}
