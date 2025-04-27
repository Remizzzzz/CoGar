Order Verifier Node
==================

**File**: ``scripts/order_verifier.py``  
**Purpose**: Validates orders with customers via voice interaction.

Subscribers:
- ``/voice_text`` (std_msgs/String): Processed speech from microphone
- ``/dish_detected`` (std_msgs/String): Confirmed dish from vision system

Publishers:
- ``/speech_output`` (std_msgs/String): Responses to customers
- ``/error_alerts`` (std_msgs/String): Dispute notifications

Service Clients:
- ``/speaker``: Uses Speaker service for audio output

Workflow:
1. Announces: "Your [Dish] is served!"
2. Listens for 5 seconds
3. If "no" heard, alerts staff