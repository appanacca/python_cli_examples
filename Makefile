run_help:
	python argparse_example.py --help  >> help.txt 2>&1
	python click_example.py --help  >> help.txt 2>&1
	python click_example_2.py --help  >> help.txt 2>&1
	python typer_example.py --help  >> help.txt 2>&1
	python fastcore_example.py --help  >> help.txt 2>&1
	python fire_example.py --help  >> help.txt 2>&1


run_cli:
	python argparse_example.py --input cat.jpg  --output cat_out.jpg  --heigth 100 --width 20 
	python click_example.py  --input cat.jpg  --output cat_out.jpg  --heigth 100 --width 20 
	python click_example_2.py   --input cat.jpg  --output cat_out.jpg  --heigth 100 --width 20 
	python typer_example.py  --input cat.jpg  --output cat_out.jpg  --heigth 100 --width 20 
	python fastcore_example.py   cat.jpg   cat_out.jpg  --heigth 100 --width 20
	python fire_example.py   --input cat.jpg  --output cat_out.jpg  --heigth 100 --width 20
