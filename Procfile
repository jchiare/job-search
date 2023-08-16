web: uvicorn applications.web.main:app --host 0.0.0.0 --port 80
service 1: uvicorn applications.data_collector.main:app --host 0.0.0.0 --port 8001
service 2: uvicorn applications.data_analysis.main:app --host 0.0.0.0 --port 8002