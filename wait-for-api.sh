#!/usr/bin/env bash
echo "Waiting for user exercises rest API to start..."

attempt_counter=0
max_attempts=12

until $(curl --output /dev/null --silent --head --fail http://api:8080); do
    if [[ ${attempt_counter} -eq ${max_attempts} ]]; then
      echo "User exercises rest API cannot reached!"
      exit 1
    fi

    printf "."
    attempt_counter=$(($attempt_counter+1))
    sleep 5
done

echo "\nUser exercises rest API has been reached! Starting tests."

behave