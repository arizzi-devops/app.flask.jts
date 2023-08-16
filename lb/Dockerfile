FROM liquibase/liquibase:${LIQUIBASE_TAG_VERSION:-4.9.1}

ENV SCRIPT=docker-entrypoint.sh

COPY docker-entrypoint.sh /liquibase/
COPY changelog.xml /liquibase/

ENTRYPOINT ["/liquibase/docker-entrypoint.sh"]
CMD ["--help"]
