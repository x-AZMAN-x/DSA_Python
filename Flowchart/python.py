"""
Consistency is very important when you are learning a new language. Committing to coding everyday will really help develop that muscle memory. Though it may seem daunting at first, consider starting small with 25 minutes everyday and working your way up from there.

As you progress on your journey as a new programmer, you should still be taking notes. In fact, research suggests that taking notes by hand is most beneficial for long-term retention. This will be especially beneficial for those working towards the goal of becoming a full-time developer, as many interviews will involve writing code on a whiteboard.

Whether you are learning about basic Python data structures (strings, lists, dictionaries, etc.) for the first time, or you are debugging an application, the interactive Python shell will be one of your best learning tools.To use the interactive Python shell (also sometimes called a “Python REPL”), first make sure Python is installed on your computer. To activate the interactive Python shell, simply open your terminal and run python or python3 depending on your installation.

When you are learning, it is important to step away and absorb the concepts. The Pomodoro Technique is widely used and can help: you work for 25 minutes, take a short break, and then repeat the process. Taking breaks is critical to having an effective study session, particularly when you are taking in a lot of new information.

When debugging, it is important to have a methodological approach to help you find where things are breaking down. Going through your code in the order in which it is executed and making sure each part works is a great way to do this.The debugger can also be run from the command line with python -m pdb <my_file.py>.

Though coding may seem like a solitary activity, it actually works best when you work together. It is extremely important when you are learning to code in Python that you surround yourself with other people who are learning as well. This will allow you to share the tips and tricks you learn along the way.

It is said that the best way to learn something is to teach it. This is true when you are learning Python. There are many ways to do this: whiteboarding with other Python lovers, writing blog posts explaining newly learned concepts, recording videos in which you explain something you learned, or simply talking to yourself at your computer.

Pair programming is a technique that involves two developers working at one workstation to complete a task. The two developers switch between being the “driver” and the “navigator.” The “driver” writes the code, while the “navigator” helps guide the problem solving and reviews the code as it is written.

Good questions can save a lot of time. Skipping any of these steps can result in back-and-forth conversations that can cause conflict. As a beginner, you want to make sure you ask good questions so that you practice communicating your thought process, and so that people who help you will be happy to continue helping you.

For beginners, there are many small exercises that will really help you become confident with Python, as well as develop the muscle memory that we spoke about above. Once you have a solid grasp on basic data structures (strings, lists, dictionaries, sets), object-oriented programming, and writing classes, it’s time to start building! What you build is not as important as how you build it.

In the open-source model, software source code is available publicly, and anyone can collaborate. There are many Python libraries that are open-source projects and take contributions. Additionally, many companies publish open-source projects.
"""

my_string = 'I am a string'
dir(my_string)
['__add__', ..., 'upper', 'zfill'] #Truncated For Readability

my_string = 'I am a string'
dir(my_string)
['__add__', ..., 'upper', 'zfill'] #Truncated For Readability

type(my_string)
str

help(str)

from datetime import datetime
dir(datetime)
['__add__', ..., 'weekday', 'year'] #Truncated For Readability
datetime.now()
datetime.datetime(2018, 3, 14, 23, 44, 50, 851904)