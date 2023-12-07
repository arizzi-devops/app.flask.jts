FROM liquibase/liquibase:${LIQUIBASE_TAG_VERSION:-4.9.1}

ENV DB_USESSL=$DB_USESSL
ENV DB_VERIFYCERT=$DB_VERIFYCERT
ENV DB_REQUIRESSL=$DB_REQUIRESSL

COPY docker-entrypoint.sh /liquibase/
COPY changelog.xml /liquibase/

ENTRYPOINT ["/liquibase/docker-entrypoint.sh"]
CMD ["--help"]
