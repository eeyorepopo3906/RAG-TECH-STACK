# RAG-TECH-STACK

## Step-by-Step Instructions : 
1. git clone repo and cd into it 
2. `pip install -r requirements.txt`
3. copy your `m3e-base` model to `models/`
4. `cd src/stremlit-web` 
5. fill `<OPENAI-API-KEY>` with your own key in the `.env` file
6. run `streamlit run demo.py` in your cli






## Deploy using Docker
1. git clone repo and cd into it 
2. copy your `m3e-base` model to `models/`
3. fill `<OPENAI-API-KEY>` with your own key in the `.env` file under `/src/streamlit-web`
4. `docker build -t my-image-name .`
5. `docker run -p 8501:8501 my-image-name`
6. visit localhost:8501
