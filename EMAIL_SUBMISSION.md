# Email Submission Template

## To: Clara Answers Team / ZenTrades AI Team

---

**Subject:** Clara Answers Intern Assignment Submission - Suneeth S

---

**Body:**

Dear Team,

I am pleased to submit my completed Clara Answers Intern Assignment. Below are my details:

### Student Information:
- **Name:** Suneeth S
- **Registration No:** 22BAI1158
- **Course:** B.Tech CSE AI ML
- **Email:** ssanapoori@gmail.com
- **Contact No:** 22BAI1158

---

### Assignment Summary

I have successfully built a **zero-cost automation pipeline** that demonstrates the complete workflow from Demo Call → Preliminary Retell Agent (v1) → Onboarding Updates → Agent Revision (v2).

#### Key Features Implemented:
1. ✅ **Pipeline A:** Demo Call Transcript → Preliminary Agent Configuration (v1)
2. ✅ **Pipeline B:** Onboarding Call → Agent Updates (v2) with Changelog
3. ✅ **Batch Processing:** Processes all 5 demo calls + 5 onboarding calls
4. ✅ **Zero-Cost:** No paid APIs used - rule-based extraction
5. ✅ **Version Control:** Maintains v1 and v2 with diff/changelog
6. ✅ **Dashboard:** Visual overview of all accounts
7. ✅ **n8n Integration:** Workflow orchestration (optional)
8. ✅ **Docker Support:** Easy local deployment

#### Project Deliverables:
- **GitHub Repository:** Complete source code
- **Demo Video:** [Loom Video Link](https://www.loom.com/share/bd423b28c0834f97ab2ac07d9a095407)
- **Account Memos:** JSON format for all 5 accounts (v1 & v2)
- **Retell Agent Specs:** Configurable JSON for Retell import
- **Changelogs:** Version diff for each account

---

### How to Run

1. **Clone the repository**
2. **Run batch processing:**
   ```
   python scripts/batch_process.py
   ```
3. **View dashboard:**
   ```
   python scripts/dashboard.py
   ```

---

### Technical Stack
- Python (scripts)
- JSON (data storage)
- n8n (workflow orchestration - optional)
- Docker (deployment)
- HTML Dashboard

---

### Additional Notes
- The pipeline handles missing information responsibly
- No hallucination - only extracts verified information
- Clear separation between demo-derived assumptions and onboarding-confirmed rules
- All outputs are reproducible

---

Thank you for this opportunity. I look forward to your feedback.

Best regards,
**Suneeth S**
B.Tech CSE AI ML
Registration No: 22BAI1158
Email: ssanapoori@gmail.com

---

## Files to Attach (if needed)
- Project ZIP file (if not using GitHub)
- README.md
- Loom Video Link


