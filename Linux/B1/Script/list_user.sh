#!bin/bash

list_user() {
	cut -d: -f1 /etc/passwd
}
