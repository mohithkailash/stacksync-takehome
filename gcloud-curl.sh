# curl -X POST \
#   http://localhost:8080/execute \
#   -H 'Content-Type: application/json' \
#   -d '{"script": "def main():\n    return {\"message\": \"Hello, World!\"}\n\nif __name__ == \"__main__\":\n    import json\n    print(json.dumps(main()))"}'

curl -X POST \
  https://python-script-executor-bsze2rjrca-uc.a.run.app/execute \
  -H 'Content-Type: application/json' \
  -d '{"script": "def main():\n    return {\"message\": \"Hello, World!\"}\n\nif __name__ == \"__main__\":\n    import json\n    print(json.dumps(main()))"}'


# curl -X POST \
#   http://localhost:8080/execute \
#   -H 'Content-Type: application/json' \
#   -d '{
#         "script": "def main(): return {\"message\": \"Hello, World!\"}"
#       }'

#   # https://python-script-executor-bsze2rjrca-uc.a.run.app/execute \
