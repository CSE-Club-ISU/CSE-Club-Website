### Structure for landing page html/template
layout.html
    navbar.html
    landing_page.html
        front_matter.html
        sponsors.html
        code_network_jobs.html
        who_are_we.html
        officers.html
        contact_us.html
    footer.html

{% extends 'layout.html' %}  # most things will extend layout
{% macro code_network_jobs() -%}  # use macros
