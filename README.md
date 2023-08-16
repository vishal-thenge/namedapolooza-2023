# \[ Auto Onboard Container as Custom Base Images \]

## Description
\[ Snyk does not support Public ECR images (https://gallery.ecr.aws/) out of the box. 
This script will allow onboarding a list of images onto Snyk and mark them as Custom base images. After that any images built on top of these base images can be onboarded onto Snyk to get custom base image recommendations. \]

## Group Members
\[ Vishal Thenge \]

## Prerequisites
\[ Snyk CLI, python 3.8. \]

## Getting Started
\[ Clone it and run the python script by passing a .txt file with a list of publicly available images you want to onboard to Snyk container . \]

### Setup
\[ set SNYK_TOKEN as a env variable pointing to the Service Account for the given Snyk Org.
Add a list of Public Images in the txt file: PublicECRImageList.txt \]

## Usage
\[ Run this as : python3 main.py <Snyk_org_id> PublicECRImageList.txt
 \]

## Features
\[  \]
