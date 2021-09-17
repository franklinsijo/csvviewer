from distutils.core import setup
setup(
  name = 'csvviewer',     
  packages = ['csvviewer'],
  version = '0.1', 
  license='MIT',  
  description = 'Command Line Delimited Text Viewer',
  author = 'franklinsijo',
  author_email = 'franklinsijo@gmail.com', 
  url = 'https://github.com/franklinsijo/csvviewer', 
  download_url = 'https://github.com/franklinsijo/csvviewer/archive/v_0.1.tar.gz', ##
  keywords = ['csv', 'command-line', 'reader'], 
  install_requires=[        
          'prettytable',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha', 
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3', 
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)