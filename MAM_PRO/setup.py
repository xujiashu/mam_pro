try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
		'description': 'collect mathematical homework tool.',
		'author': 'Xujiashu',
		'url': 'https://github.com/xujiashu/mam_pro', 
		'email': '13760701536@163.com',
		'version': 0.01,
		'install_requites': [],
		'packages': [],
		'scripts': [],
		'name': 'MAM_PRO'
}

setup(**config)

