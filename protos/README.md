# mFit Protocol Buffer Compiler

## Getting Started
### Pulling
Pull the image.
```
sudo docker pull dnguyen0304/mfit-protos-buildtime:latest
```

### Running
Run an example.
```
sudo docker run --rm \
                --volume $(pwd):/tmp/build \
                dnguyen0304/mfit-protos-buildtime:latest \
                --help
```

```
# NOTE: Remember to replace the <file path> placeholder.

sudo docker run --rm \
                --volume $(pwd):/tmp/build \
                dnguyen0304/mfit-protos-buildtime:latest \
                --proto_path . \
                --python_out . \
                mfit/protos/<file name>
```

## Advanced
### Building
Build the image.
```
sudo docker build --file Dockerfile \
                  --tag dnguyen0304/mfit-protos-buildtime:latest \
                  .
```

### Pushing
Push the image.
```
sudo docker push dnguyen0304/mfit-protos-buildtime:latest
```
