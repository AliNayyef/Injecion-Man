from setuptools import setup, find_packages

setup(
    name='Injection-Man',  
    version='1.0.0',  
    packages=find_packages(), 
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'injection-man=injection_man.main:main',  
        ],
    },
    description='''
    Injecion-Man: XSS & SQL Injection Exploiter (XSS-SQLi-Exploit)
    
    Description:
    The XSS & SQL Injection Exploiter is a Python-based tool designed for security researchers,
    ethical hackers, and penetration testers to identify and demonstrate vulnerabilities in web applications.
    This tool specifically targets two common web application security vulnerabilities:

    Cross-Site Scripting (XSS):
    XSS vulnerabilities allow attackers to inject malicious scripts into trusted websites. This tool helps detect and demonstrate stored, 
    reflected (time-based, error-based) injection.

    SQL Injection (SQLi):
    SQL Injection vulnerabilities enable attackers to manipulate backend databases by injecting malicious SQL code into an application’s query. 
    This tool automates the process of identifying and exploiting SQLi weaknesses by submitting common SQL injection payloads to URL parameters.
    
    Features:
    Multiple Payload Support:
    Includes a variety of pre-built XSS and SQLi payloads, such as:

    XSS payloads to execute malicious scripts in the victim’s browser.
    SQLi payloads to manipulate database queries and extract sensitive information.
    
    ''',
    author='Ali Yousif Nayyef',
    author_email='ali.nayyef.contact@gmail.com',
    url='www.linkedin.com/in/ali-nayyef',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
