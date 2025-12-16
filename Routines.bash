#!/usr/bin/env bash
set -e -x
rotname=$1

SENSIBLE_TIMEOUT=$((5*60))

case $rotname in
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
  
  reinvent_wheel)
    python3 -m pip install --upgrade build
    pushd AssertMixins/
    python3 -m build
    popd
    ;;
  publish_wheel)
    python3 -m pip install --upgrade twine
    pushd AssertMixins/
    python3 -m twine upload --repository pypi dist/*
    popd
    ;;
	
  *)
    set +x
    echo Unknown routine name $rotname...
    echo Valid routine names would be:
    sed -n -e '/^case \$rotname in$/,/^esac$/p' $0 | grep -o '^ *[^*)]\+)$' | grep -o '[^*) ][^*)]*' | sed -e 's/^/ - /'
    exit -1
    ;;
esac
