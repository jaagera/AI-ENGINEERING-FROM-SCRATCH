NOTE: Every AI API works the same way: send a request, get a response. The details change, the pattern doesn't.

# Every API call has:
    An endpoint (URL)
    An API key (authentication)
    A request body (what you want)
    A response body (what you get back)

The code that gets committed only names the variable; the value lives in a gitignored .env file and is injected into the process environment at runtime, then sent as an Authorization header. If the key ever appears in the source, it ships with every clone of the repo, and a leaked key bills to your account.

# STEPS ON WORKING WITH API KEYS SAFELY
1. Store API keys safely: Never put API keys in code. Use environment variables.
2. First API call(Python)
3. First API call (Typescript)
4. Raw HTTP(Hypertex Transfer Protocol)(No SDK(Software Development Kit))
# THE BIG QUESTION?
How does my code talk to a model running on someone else’s server, safely? The four objectives are the four parts of the answer.
1. Store API keys securely
What an API key is: a secret string (like sk-ant-...) tied to your account. Anyone who has it can spend your money.
The rule: never put a key in your source code.
*** You need to know three things about it:***
(a). Add .env to .gitignore immediately, before your first commit. This is the most important habit in the lesson.
(b). Load it in Python with python-dotenv:
Commit a .env.example with fake values (ANTHROPIC_API_KEY=your-key-here) so others know which variables the project needs.
2. Make an API call two ways
With the SDK (the easy way)

* Things you need to understand:
The request has three parts: the URL (endpoint), the headers (your key and API version), and the JSON body (model, max_tokens, messages).
max_tokens is required. It caps the length of the reply.
messages is a list of {role, content} objects. Roles are user and assistant. This list is how conversations work: you send the whole history every time, because the API remembers nothing between calls.
The response has a content list of blocks, and the text is at response.content[0].text. It also includes usage (input and output token counts) and stop_reason.
A system prompt goes in a separate system field, not inside messages.
3. Why compare SDK and raw HTTP?
This is a debugging skill. The SDK hides details, so when something breaks you need to see what is really being sent and received.
4. Common errors and how to handle them
Learn these status codes, because you will meet all of them:

Code	Meaning	Usual cause	                                                What to do
400	    Bad request	Malformed JSON, missing max_tokens, bad parameters	    Read the error message and fix the request
401	    Authentication error	Missing, wrong, or revoked key	            Check the key and the env variable
403	    Permission denied	Key lacks access to that resource	            Check account and permissions
404	    Not found	Wrong model name or endpoint	                        Check the current model list in the docs
429	    Rate limited	Too many requests or tokens per minute	            Wait and retry with backoff
500 / 529	Server error or overloaded	Problem on the provider’s side	    Retry after a pause
# Things to know:
API key: a secret credential that identifies and bills your account
Environment variable: a value stored outside your code and read at runtime
.env file: a local file that holds environment variables, never committed
Endpoint: the URL you send requests to
Token: a chunk of text (roughly 3/4 of a word) that models read and write, and what you are billed for
Rate limit: a cap on how many requests or tokens you can use per minute
Exponential backoff: waiting longer after each failed retry