# MiniHack-2023

## The Story
The purpose of the Cal Poly Pomona MiniHack 2023 was to leverage the OpenAI API to create a simple chatbot with the GPT-3 API. I completed the challenge and pushed further, developing several additional features designed to push my knowlege of both frontend and backend programming. Some of the features I implemented were:
- A web interface instead of a terminal-based one
- An API to separate the web interface from sensative server components
- Text-to-speech capabilities to allow visually-impared users to access the site
- DALLE-2 integration, so the user can generate images with prompts prefixed with ``image:``

Overall, the project helped me expand my understanding of Flask, a python-based API development framework, the central three web development languages (JS, HTML, CSS), and integrating projects with other APIs.

## If you want to test this project for yourself:
1) Clone the repo onto your local machine
2) Get an API key from OpenAI [https://www.maisieai.com/help/how-to-get-an-openai-api-key-for-chatgpt](Tutorial)
3) Create a file named ``.env``
4) On the first line, put ``OPENAI-KEY=[your_api_key]``, and save and close the file 
5) Run ``main.py``
6) Go to the ip address that opens up in your browser and start playing around! (make sure to have your volume up)
