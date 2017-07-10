import json
import bs4
import requests
import re
import logging as log
from abc import ABCMeta, abstractmethod
import sys

class InstagramUser:
    def __init__(self, user_id, username=None, bio=None, followers_count=None, following_count=None, is_private=False):
       
        """
        self.id = user_id
        self.username = username
        self.bio = bio
        self.followers_count = followers_count
        self.following_count = following_count
        self.is_private = is_private

        """
class InstagramPost:
    def __init__(self, post_id, code, user=None, caption="", display_src=None, is_video=False, created_at=None):
        """
        A class to represent a post on Instagram
        :param post_id: ID of the post
        :param code: Code of the post
        :param user: A user object representing the owner of the post
        :param caption: The caption/text of the post
        :param display_src: The URL of the image of the post
        :param is_video: A boolean value indicating it's a video
        :param created_at: The time it was created
        """
        self.post_id = post_id
        self.code = code
        self.caption = caption
        self.user = user
        self.display_src = display_src
        self.is_video = is_video
        self.created_at = created_at