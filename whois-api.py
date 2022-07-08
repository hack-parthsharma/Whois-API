#!/usr/bin/env python
# -*- coding: utf-8 -*-
# glenn@sensepost.com // @glennzw
from flask import Flask, jsonify
import whois
import validators

app = Flask(__name__)

@app.route('/whois/<domain>')
def whoiser(domain):
    if not validators.domain(domain):
        return jsonify({"Error" : "Invalid domain"})
    try:
        w = whois.whois(domain)
    except Exception, e:
        return jsonify({"Error" : "Unable to lookup domain"})
    return jsonify(w)

if __name__ == '__main__':
    app.run()
