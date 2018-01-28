#!/bin/bash
#

if [ -z $SWAGGER_CODEGEN_PATH ]; then
    # current directory is default if no path given?
    SWAGGER_CODEGEN_PATH="."
fi

if [ -z $SWAGGER_CODEGEN_EXEC ]; then
    SWAGGER_CODEGEN_EXEC="java -jar $SWAGGER_CODEGEN_PATH/swagger-codegen-cli.jar"
fi

if [ "$#" -lt 1 ]; then
    echo "generate-client.sh <path to specification file>"
else
    $SWAGGER_CODEGEN_EXEC generate  \
    -i $1                           \
    -l python                       \
    -o ../client                    \
    --skip-overwrite
fi
