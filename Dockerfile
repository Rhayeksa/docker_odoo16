FROM odoo:16
USER root
COPY ./custom_addons /var/lib/odoo/addons/16.0/custom_addons
RUN rm /etc/odoo/odoo.conf
COPY ./config/odoo.conf /etc/odoo
# ENV HOST=127.0.0.1
ENV USER=odoo16
ENV PASSWORD=odoo16
# EXPOSE 8099

# FROM postgres:15
# ENV POSTGRES_DB=postgres
# ENV POSTGRES_PASSWORD=odoo12
# ENV POSTGRES_USER=odoo12
# EXPOSE 5433

# TODO: buat image yang sudah include postgres database pada Odoo atau buat 2 image dalam 1 dockerfile