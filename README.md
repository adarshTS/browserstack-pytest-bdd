# pytest-bdd-browserstack-example
Example project for executing pytest-bdd framework on BrowserStack


### Install the dependencies

To install the dependencies, run :

- For Python 3

    ```sh
    pip3 install -r requirements.txt
    ```

- For Python 2

    ```sh
    pip2 install -r requirements.txt
    ```



## Getting Started

Getting Started with pytest-bdd  on real BrowserStack couldn't be easier!

### **Run first test :**

- Include the access key as environment variables

    ```sh
        export BROWSERSTACK_USER=<Your user name>
        export BROWSERSTACK_ACCESS_KEY=<Your access Key>
    ```

- For all versions of python

	```sh
		pytest testGoogleSrch.py -v
	```	