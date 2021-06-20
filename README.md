# AI Redis Queue Template


### Run redis
```bash
docker run -p 6379:6379 redis
```

### Run workers
```bash
python src/worker.py
```

### Run task creator
```bash
python src/creator.py
```