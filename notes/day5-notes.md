## Day 5 Notes

### Observation Questions:
- Turn 2 rewritten as: "What formats does NexusChat support?" — correctly resolved 'it'.
- Without rewriting, raw query 'What formats does it support?' retrieves wrong chunks.
- We rewrite for retrieval but pass original to generation so response feels natural.

### Turn Results:
- Turn 1: "What is NexusChat?" — grounded answer citing sample.pdf 
- Turn 2: "What formats does it support?" — rewritten correctly 
- Turn 3: "Professional plan cost?" — retrieved from sample2.txt, 200 USD 
- Turn 4: "Does that include support?" — resolved to Professional plan, priority support 