def my_func(job_name, job_ID, out){

    echo (job_name)

    echo (job_ID)

    echo (out)

}
 
def out = ""
 
 
pipeline {

    agent any


    parameters {

    string defaultValue: 'pipeline.zip', description: 'This is description.', name: 'EMA'

    string defaultValue: 'pipeline', description: 'This is branch.', name: 'GIT_BRANCH'

    booleanParam description: 'This is boolean description', name: 'FAIL_PIPELINE'

    booleanParam description: 'This is run test param', name: 'RUN_TEST'

    booleanParam description: 'This is send email param', name: 'SEND_EMAIL'

    }

    stages {

        stage('Download'){

            steps {

                cleanWs()
               withCredentials([usernamePassword(credentialsId: 'ebug', passwordVariable: 'PASS', usernameVariable: 'CRED')]) {
               echo("$CRED $PASS")
                }

                echo (message : "Download")

                dir('pipeline')

                {

                    git (

                        branch: 'pipeline',

                        url: 'https://github.com/KLevon/jenkins-course'

                    )

                }

                rtDownload(

                    serverId: 'Artifactory',

                    spec: ''' {

                          "files": [

                          {

                            "pattern": "generic-local/libraries/printer.zip",

                            "target": "printer/printer.zip"

                          }

                        ]

                     }'''

                )

                unzip (

                    zipFile: "printer/libraries/printer.zip",

                    dir: "pipeline"

                    )

            }

        }

                stage('Build'){

            steps {

                echo (message : "Build")

                bat(

                    script: """

                        cd pipeline

                        Makefile.bat

                    """

                    )

            }

        }

        stage('Tests'){

            when {

                equals expected: true,

                actual:params.RUN_TEST

            }

            steps {

                echo (message : "Build")

                script{

                def array = ['printer', 'scanner', 'main']

                for (element in array)

                {

                        out += bat(

                        script: """

                            pipeline/Tests.bat $element

                        """, returnStdout: true

                        ).trim()

                    }   

                }

            }

        }

                stage('Publish'){

            steps {

                echo (message : "Publish")

                script{

                    zip (

                        zipFile: "${EMA}.zip",

                        archive: true,

                        dir: "pipeline"

                    ) 

                }

                rtUpload(

                    serverId: 'Artifactory',

                    spec: """ {

                          "files": [

                          {

                            "pattern": "${EMA}.zip",

                            "target": "generic-local/jovana/${env.BUILD_ID}/${EMA}.zip"

                          }

                        ]

                     }"""

                )

                script{

                if (FAIL_PIPELINE == "true")

                    {

                        bat(

                        script: """

                            bat exit 1

                        """

                        )

                    } 

           //         my_func(env.JOB_NAME, env.BUILD_ID)

                }

 
            }

        }

    }

    post {

        success{

            script{

                if (params.SEND_EMAIL == true)

                    {

                        my_func(env.JOB_NAME, env.BUILD_ID, out)

                    } 

           //         my_func(env.JOB_NAME, env.BUILD_ID)

                }

        }

    }

}

 
