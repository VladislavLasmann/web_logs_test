from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def test_api_json(request):
    test_logs_dict = {
        "id": "111111",
        "apiEndpointCall": "/testapi param1 param2",
        "status": "running",
        "shellExecutionSummary": {
            "command": "/testthat site hde03e",
            "logs":
                """
                Downloading numpy-1.17.2-cp37-cp37m-manylinux1_x86_64.whl (20.3 MB)
Collecting packaging==19.1
  Downloading packaging-19.1-py2.py3-none-any.whl (30 kB)
Requirement already satisfied: pandas==1.0.3 in /usr/local/lib/python3.7/site-packages (from -r requirements.txt (line 25)) (1.0.3)
Collecting pika==1.1.0
  Downloading pika-1.1.0-py2.py3-none-any.whl (148 kB)
Collecting prompt-toolkit==3.0.5
  Downloading prompt_toolkit-3.0.5-py3-none-any.whl (351 kB)
Collecting psycopg2==2.8.4
  Downloading psycopg2-2.8.4.tar.gz (377 kB)
Collecting Pygments==2.3.1
  Downloading Pygments-2.3.1-py2.py3-none-any.whl (849 kB)
Collecting pymongo==3.9.0
  Downloading pymongo-3.9.0-cp37-cp37m-manylinux1_x86_64.whl (447 kB)
Collecting pyparsing==2.4.2
  Downloading pyparsing-2.4.2-py2.py3-none-any.whl (65 kB)
Collecting python-dateutil==2.8.0
  Downloading python_dateutil-2.8.0-py2.py3-none-any.whl (226 kB)
Collecting pytz==2019.2
  Downloading pytz-2019.2-py2.py3-none-any.whl (508 kB)
Collecting recommonmark==0.6.0
  Downloading recommonmark-0.6.0-py2.py3-none-any.whl (10 kB)
Collecting requests==2.22.0
  Downloading requests-2.22.0-py2.py3-none-any.whl (57 kB)
Collecting six==1.12.0
  Downloading six-1.12.0-py2.py3-none-any.whl (10 kB)
Collecting snowballstemmer==1.9.0
  Downloading snowballstemmer-1.9.0.tar.gz (76 kB)
Collecting Sphinx==2.2.0
  Downloading Sphinx-2.2.0-py3-none-any.whl (3.3 MB)
Collecting sphinxcontrib-applehelp==1.0.1
  Downloading sphinxcontrib_applehelp-1.0.1-py2.py3-none-any.whl (121 kB)
Collecting sphinxcontrib-devhelp==1.0.1
  Downloading sphinxcontrib_devhelp-1.0.1-py2.py3-none-any.whl (84 kB)
Collecting sphinxcontrib-htmlhelp==1.0.2
  Downloading sphinxcontrib_htmlhelp-1.0.2-py2.py3-none-any.whl (96 kB)
Collecting sphinxcontrib-jsmath==1.0.1
  Downloading sphinxcontrib_jsmath-1.0.1-py2.py3-none-any.whl (5.1 kB)
Collecting sphinxcontrib-qthelp==1.0.2
  Downloading sphinxcontrib_qthelp-1.0.2-py2.py3-none-any.whl (90 kB)
Collecting sphinxcontrib-serializinghtml==1.1.3
  Downloading sphinxcontrib_serializinghtml-1.1.3-py2.py3-none-any.whl (89 kB)
Collecting SQLAlchemy==1.3.10
  Downloading SQLAlchemy-1.3.10.tar.gz (6.0 MB)
Collecting typing-extensions==3.7.4.1
  Downloading typing_extensions-3.7.4.1-py3-none-any.whl (20 kB)
Collecting urllib3==1.25.3
  Downloading urllib3-1.25.3-py2.py3-none-any.whl (150 kB)
Collecting wcwidth==0.1.7
  Downloading wcwidth-0.1.7-py2.py3-none-any.whl (21 kB)
Requirement already satisfied: setuptools in /usr/local/lib/python3.7/site-packages (from kiwisolver==1.1.0->-r requirements.txt (line 18)) (46.1.3)
Building wheels for collected packages: future, psycopg2, snowballstemmer, SQLAlchemy
  Building wheel for future (setup.py): started
  Building wheel for future (setup.py): finished with status 'done'
  Created wheel for future: filename=future-0.17.1-py3-none-any.whl size=488732 sha256=fcaa9e74b89e263474fe350bfd81702bf7f4e58650a6d9f7a4c56b88b8c6b6e1
  Stored in directory: /root/.cache/pip/wheels/16/4c/84/8a6161d44282ede60ed233d090156c6109a7ab865e49c1c9f6
  Building wheel for psycopg2 (setup.py): started
  Building wheel for psycopg2 (setup.py): finished with status 'done'
  Created wheel for psycopg2: filename=psycopg2-2.8.4-cp37-cp37m-linux_x86_64.whl size=466682 sha256=08f008919f13d8276711bbf55f97f8090d13e2d4d7ae2a7b0c0f4608801e107b
  Stored in directory: /root/.cache/pip/wheels/e5/95/7b/9065a4dfe97a9b0e458215ea04fa87c169e20c9bddf49f766a
  Building wheel for snowballstemmer (setup.py): started
  Building wheel for snowballstemmer (setup.py): finished with status 'done'
  Created wheel for snowballstemmer: filename=snowballstemmer-1.9.0-py3-none-any.whl size=93832 sha256=25c1f59005ef07a1090c442ce88997fe0bc924bb3042dbe0ce2cd804fe4ea81d
  Stored in directory: /root/.cache/pip/wheels/bb/f4/05/5206042fdf39c55e94131ac203541f48ceedc203e9a61b3b62
  Building wheel for SQLAlchemy (setup.py): started
  Building wheel for SQLAlchemy (setup.py): finished with status 'done'
  Created wheel for SQLAlchemy: filename=SQLAlchemy-1.3.10-cp37-cp37m-linux_x86_64.whl size=1206957 sha256=bec43ed6cf2c6139a3377adb3bf8720d2ed2616b2e9c1f2f97c93ed68e755381
  Stored in directory: /root/.cache/pip/wheels/7a/dd/8c/79eb1ca5a4e2edb32e9390d746dc4fc4c4f8eaeeb5491da779
Successfully built future psycopg2 snowballstemmer SQLAlchemy
Installing collected packages: alabaster, six, python-dateutil, arrow, attrs, pytz, Babel, certifi, chardet, Click, colorama, future, commonmark, coverage, croniter, cycler, docutils, idna, imagesize, MarkupSafe, Jinja2, kiwisolver, lxml, pyparsing, numpy, matplotlib, mock, packaging, pika, wcwidth, prompt-toolkit, psycopg2, Pygments, pymongo, sphinxcontrib-serializinghtml, sphinxcontrib-qthelp, sphinxcontrib-htmlhelp, sphinxcontrib-jsmath, sphinxcontrib-devhelp, urllib3, requests, sphinxcontrib-applehelp, snowballstemmer, Sphinx, recommonmark, SQLAlchemy, typing-extensions
  Attempting uninstall: six
    Found existing installation: six 1.14.0
    Uninstalling six-1.14.0:
      Successfully uninstalled six-1.14.0
  Attempting uninstall: python-dateutil
    Found existing installation: python-dateutil 2.8.1
    Uninstalling python-dateutil-2.8.1:
      Successfully uninstalled python-dateutil-2.8.1
  Attempting uninstall: pytz
    Found existing installation: pytz 2019.3
    Uninstalling pytz-2019.3:
      Successfully uninstalled pytz-2019.3
  Attempting uninstall: numpy
    Found existing installation: numpy 1.18.2
    Uninstalling numpy-1.18.2:
      Successfully uninstalled numpy-1.18.2
Successfully installed Babel-2.7.0 Click-7.0 Jinja2-2.10.1 MarkupSafe-1.1.1 Pygments-2.3.1 SQLAlchemy-1.3.10 Sphinx-2.2.0 alabaster-0.7.12 arrow-0.15.5 attrs-19.1.0 certifi-2019.6.16 chardet-3.0.4 colorama-0.4.1 commonmark-0.9.0 coverage-4.5.4 croniter-0.3.30 cycler-0.10.0 docutils-0.15.2 future-0.17.1 idna-2.8 imagesize-1.1.0 kiwisolver-1.1.0 lxml-4.4.1 matplotlib-3.1.1 mock-3.0.5 numpy-1.17.2 packaging-19.1 pika-1.1.0 prompt-toolkit-3.0.5 psycopg2-2.8.4 pymongo-3.9.0 pyparsing-2.4.2 python-dateutil-2.8.0 pytz-2019.2 recommonmark-0.6.0 requests-2.22.0 six-1.12.0 snowballstemmer-1.9.0 sphinxcontrib-applehelp-1.0.1 sphinxcontrib-devhelp-1.0.1 sphinxcontrib-htmlhelp-1.0.2 sphinxcontrib-jsmath-1.0.1 sphinxcontrib-qthelp-1.0.2 sphinxcontrib-serializinghtml-1.1.3 typing-extensions-3.7.4.1 urllib3-1.25.3 wcwidth-0.1.7
Got YFHttpException 'HttpException on yahoo finance api. Response Code: 401'. Now trying again.
Got YFHttpException 'HttpException on yahoo finance api. Response Code: 401'. Now trying again.
Got YFHttpException 'HttpException on yahoo finance api. Response Code: 401'. Now trying again.
Got YFHttpException 'HttpException on yahoo finance api. Response Code: 401'. Now trying again.
Got YFHttpException 'HttpException on yahoo finance api. Response Code: 401'. Now trying again.
Got YFHttpException 'HttpException on yahoo finance api. Response Code: 401'. Now trying again.
Got YFHttpException 'HttpException on yahoo finance api. Response Code: 401'. Now trying again.
Got YFHttpException 'HttpException on yahoo finance api. Response Code: 401'. Now trying again.
Got YFHttpException 'HttpException on yahoo finance api. Response Code: 401'. Now trying again.
Got YFHttpException 'HttpException on yahoo finance api. Response Code: 401'. Now trying again.
Got YFHttpException 'HttpException on yahoo finance api. Response Code: 401'. Now trying again.
Got YFHttpException 'HttpException on yahoo finance api. Response Code: 401'. Now trying again.
Got YFHttpException 'HttpException on yahoo finance api. Response Code: 401'. Now trying again.
Successfully installed Babel-2.7.0 Click-7.0 Jinja2-2.10.1 MarkupSafe-1.1.1 Pygments-2.3.1 SQLAlchemy-1.3.10 Sphinx-2.2.0 alabaster-0.7.12 arrow-0.15.5 attrs-19.1.0 certifi-2019.6.16 chardet-3.0.4 colorama-0.4.1 commonmark-0.9.0 coverage-4.5.4 croniter-0.3.30 cycler-0.10.0 docutils-0.15.2 future-0.17.1 idna-2.8 imagesize-1.1.0 kiwisolver-1.1.0 lxml-4.4.1 matplotlib-3.1.1 mock-3.0.5 numpy-1.17.2 packaging-19.1 pika-1.1.0 prompt-toolkit-3.0.5 psycopg2-2.8.4 pymongo-3.9.0 pyparsing-2.4.2 python-dateutil-2.8.0 pytz-2019.2 recommonmark-0.6.0 requests-2.22.0 six-1.12.0 snowballstemmer-1.9.0 sphinxcontrib-applehelp-1.0.1 sphinxcontrib-devhelp-1.0.1 sphinxcontrib-htmlhelp-1.0.2 sphinxcontrib-jsmath-1.0.1 sphinxcontrib-qthelp-1.0.2 sphinxcontrib-serializinghtml-1.1.3 typing-extensions-3.7.4.1 urllib3-1.25.3 wcwidth-0.1.7
                """,
            "returnCode": "0",
        }
    }
    return JsonResponse(test_logs_dict)
