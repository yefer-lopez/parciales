
from models.acortador import acort
from config.database import db
from flask import Flask, render_template, request, redirect, url_for, flash,session

def acortar():
    forms=acort.acortarlink()
    return  forms