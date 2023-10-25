#!/bin/bash
set -e

generate_liquibase_props() {
    props_file="/liquibase/liquibase.docker.properties"
    cat <<EOF > "$props_file"
liquibase.command.url: jdbc:mysql://${DB_HOST}:${DB_PORT:-3306}/${DB_NAME}?useSSL=${DB_USESSL:-false}&requireSSL=${DB_REQUIRESSL:-true}&verifyServerCertificate=${DB_VERIFYCERT:-false}
liquibase.command.username: ${DB_USER_ADM}
liquibase.command.password: ${DB_PASSWORD_ADM}

classpath: mysql-connector-java.jar
EOF
    echo "$props_file"
}

# Function to cleanup Liquibase properties file
cleanup_liquibase_props() {
    if [ -f "$1" ]; then
        rm -f "$1"
        echo "Liquibase properties file deleted"
    fi
}

# Generate Liquibase properties file
liquibase_props_file=$(generate_liquibase_props)
if [[ "$1" != "history" ]] && type "$1" > /dev/null 2>&1; then
    # Command execution
    trap "{ cleanup_liquibase_props $liquibase_props_file; }" EXIT
else
    if [[ "$*" == *--defaultsFile* ]] || [[ "$*" == *--defaults-file* ]] || [[ "$*" == *--version* ]]; then
        # Run as-is
        /liquibase/liquibase "$@"
    else
        # Include standard defaultsFile
        /liquibase/liquibase "--defaultsFile=/liquibase/liquibase.docker.properties" "--changelog-file=changelog.xml" "$@"
    fi
fi
