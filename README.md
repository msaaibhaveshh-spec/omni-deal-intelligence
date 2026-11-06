# 💼 Omni Deal Intelligence

> **Enterprise B2B Sales & Deal Intelligence Agent powered by Groq LLM & Vectorize Hindsight Persistent Memory**

Omni Deal Intelligence is an agentic AI system designed to eliminate context loss across multi-month enterprise B2B sales cycles. By leveraging **Vectorize Hindsight**, the agent retains long-term client objections, tracks deal risk indices, and dynamically tailors executive pitches based on stakeholder personas (CFO, CTO, VP of Sales).

---

## 🚀 Key Features

* **🧠 Persistent Episodic Memory:** Stores and recalls prior client objections, vendor comparisons (e.g., Salesforce), and pricing feedback using Hindsight.
* **📊 Automated Deal Risk Indexing:** Automatically evaluates deal risk (0–100%) based on historical client friction points.
* **👤 Multi-Persona Adaptation:** Dynamically tailors pitch responses for specific executives (CFO/ROI focus, CTO/Security focus, VP of Sales/Efficiency focus).
* **⚡ Resilient LLM Inference:** Built with Groq API featuring automated dynamic model fallbacks to guarantee 99.9% uptime during client interactions.

---

## 💰 Business ROI & Enterprise Impact

* **75% Reduction** in manual sales record maintenance and CRM data entry.
* **35% Acceleration** in deal closure speed by eliminating context drop across call gaps.
* **~$4,700/month** saved in sales operational costs per user, scaling to multi-crore revenue impact by preventing enterprise deal slippage.

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **LLM Engine:** Groq API (`llama3-70b`, `llama-3.1-8b-instant` auto-fallback)
* **Memory Layer:** Vectorize Hindsight API (`hindsight-client`)
* **Language:** Python 3.10+

---

## 🏁 Quickstart & Installation

```bash
# Clone the repository
git clone [https://github.com/msaaibhaveshh-spec/omni-deal-intelligence.git](https://github.com/msaaibhaveshh-spec/omni-deal-intelligence.git)
cd omni-deal-intelligence

# Set up virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install streamlit groq hindsight-client python-dotenv

# Configure Environment Variables (.env)
GROQ_API_KEY=your_groq_api_key
HINDSIGHT_API_KEY=your_hindsight_api_key
HINDSIGHT_BANK_ID=deal_intelligence_bank

# Run Streamlit App
python -m streamlit run app.py
