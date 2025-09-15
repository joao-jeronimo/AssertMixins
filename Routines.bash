#!/usr/bin/env bash
set -e -x

SENSIBLE_TIMEOUT=$((5*60))

case $1 in
  deps_devel)
    pushd AssertMixins/
    python3 -m pip install --upgrade -r requirements.txt
    popd
    ;;
    
  install_program)
    pushd AssertMixins/
    pip install -e .
    popd
    ;;
    
  test_unit)
    pushd AssertMixins/
    pytest --timeout=$SENSIBLE_TIMEOUT
    popd
    ;;
	
  full_local_test)
    # Clear the screen:
    reset; clear
    # Add modifications, update editable installations and run tests, in order:
    git add .
    pushd AssertMixins/
    pip install -e .
    pytest --timeout=$SENSIBLE_TIMEOUT
    # Always return to oeiginal directory:
    popd
    ;;
	
  *)
    echo "Unknown routine name: $1"
    exit -1
    ;;
esac
