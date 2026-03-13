<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Event Markdown Generator</title>
  <style>
    :root {
      --bg: #f4f7fb;
      --card: #ffffff;
      --text: #1f2937;
      --muted: #6b7280;
      --border: #d1d5db;
      --primary: #0f2d5c;
      --primary-hover: #0b2347;
      --accent: #eef4ff;
      --success: #0f766e;
    }

    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      font-family: Arial, Helvetica, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.5;
    }

    .container {
      max-width: 1100px;
      margin: 0 auto;
      padding: 16px;
    }

    h1, h2, h3 {
      margin-top: 0;
    }

    .header {
      margin-bottom: 16px;
    }

    .header p {
      color: var(--muted);
      margin: 6px 0 0;
    }

    .grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 16px;
    }

    @media (min-width: 900px) {
      .grid {
        grid-template-columns: 1.1fr 0.9fr;
      }
    }

    .card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 16px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    }

    .section-title {
      font-size: 1.1rem;
      margin-bottom: 12px;
      color: var(--primary);
    }

    .form-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 12px;
    }

    @media (min-width: 640px) {
      .form-grid.two {
        grid-template-columns: 1fr 1fr;
      }
    }

    label {
      display: block;
      font-weight: 600;
      margin-bottom: 6px;
    }

    input[type="text"],
    input[type="datetime-local"],
    input[type="date"],
    textarea,
    select {
      width: 100%;
      padding: 10px 12px;
      border: 1px solid var(--border);
      border-radius: 8px;
      font: inherit;
      background: white;
      color: var(--text);
    }

    textarea {
      min-height: 90px;
      resize: vertical;
    }

    .checkbox-row {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-top: 8px;
    }

    .help {
      color: var(--muted);
      font-size: 0.92rem;
      margin-top: 4px;
    }

    .button-row {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 16px;
    }

    button {
      border: none;
      border-radius: 8px;
      padding: 10px 16px;
      font: inherit;
      font-weight: 700;
      cursor: pointer;
    }

    .primary {
      background: var(--primary);
      color: white;
    }

    .primary:hover {
      background: var(--primary-hover);
    }

    .secondary {
      background: #e5e7eb;
      color: #111827;
    }

    .secondary:hover {
      background: #d1d5db;
    }

    .success {
      background: var(--success);
      color: white;
    }

    .preview {
      white-space: pre-wrap;
      background: #0b1020;
      color: #ecf2ff;
      border-radius: 10px;
      padding: 14px;
      min-height: 500px;
      overflow-x: auto;
      font-family: Consolas, Monaco, monospace;
      font-size: 0.92rem;
    }

    .pill {
      display: inline-block;
      padding: 4px 8px;
      border-radius: 999px;
      background: var(--accent);
      color: var(--primary);
      font-size: 0.85rem;
      font-weight: 700;
      margin-bottom: 8px;
    }

    .small {
      font-size: 0.9rem;
      color: var(--muted);
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1>Event Markdown Generator</h1>
      <p>Create a Markdown file with front matter and HTML body matching your event page format.</p>
    </div>

    <div class="grid">
      <div class="card">
        <div class="pill">Input Form</div>
        <h2 class="section-title">Front Matter</h2>

        <div class="form-grid two">
          <div>
            <label for="title">Title</label>
            <input id="title" type="text" value="FLL Challenge Summer Camp" />
          </div>
          <div>
            <label for="layout">Layout</label>
            <input id="layout" type="text" value="event" />
          </div>
        </div>

        <div class="form-grid two">
          <div>
            <label for="date">Date/Time Published</label>
            <input id="date" type="datetime-local" value="2026-02-01T12:00" />
            <div class="help">Timezone offset is added separately below.</div>
          </div>
          <div>
            <label for="timezone">Timezone Offset</label>
            <input id="timezone" type="text" value="-05:00" />
          </div>
        </div>

        <div class="form-grid">
          <div>
            <label for="short_description">Short Description</label>
            <textarea id="short_description">Join our FLL Challenge Summer Camp! Students will learn robot building, coding, robot game strategy, innovation project skills, and teamwork in a fun FTC-led week of robotics.</textarea>
          </div>
        </div>

        <div class="form-grid">
          <div>
            <label for="page_header_image">Page Header Image</label>
            <input id="page_header_image" type="text" value="images/events/FLL_Challenge_Summer_Camp.jpg" />
          </div>
        </div>

        <div class="form-grid">
          <div>
            <label for="description">Description</label>
            <textarea id="description">FIRST LEGO League (FLL) Challenge is a hands-on STEM program where students build and program LEGO robots, solve missions, develop an innovation project, and practice teamwork through Core Values. Our FTC team will teach and guide students through the full FLL Challenge experience during this summer camp.</textarea>
          </div>
        </div>

        <div class="form-grid two">
          <div>
            <label for="stripe_url">Stripe URL</label>
            <input id="stripe_url" type="text" value="" />
          </div>
          <div>
            <label for="event_dates">Event Dates</label>
            <input id="event_dates" type="text" value="2026-06-15, 2026-06-16, 2026-06-17, 2026-06-18, 2026-06-19" />
            <div class="help">Comma-separated dates.</div>
          </div>
        </div>

        <div class="form-grid two">
          <div>
            <label for="time">Time</label>
            <input id="time" type="text" value="8:00 AM – 12:00 PM" />
          </div>
          <div>
            <label for="location">Location</label>
            <input id="location" type="text" value="2171 Ivy Road, Charlottesville, VA" />
          </div>
        </div>

        <div class="form-grid two">
          <div>
            <label for="draft">Draft</label>
            <select id="draft">
              <option value="false" selected>false</option>
              <option value="true">true</option>
            </select>
          </div>
          <div>
            <label for="filename">Download Filename</label>
            <input id="filename" type="text" value="fll-challenge-summer-camp.md" />
          </div>
        </div>

        <h2 class="section-title" style="margin-top: 24px;">Body Content</h2>

        <div class="form-grid two">
          <div>
            <label for="overview_heading">Overview Heading</label>
            <input id="overview_heading" type="text" value="FLL Challenge Summer Camp Overview" />
          </div>
          <div>
            <label for="theme">Theme / Focus</label>
            <input id="theme" type="text" value="Full FLL Challenge Experience" />
          </div>
        </div>

        <div class="form-grid two">
          <div>
            <label for="when_text">When</label>
            <input id="when_text" type="text" value="June 15–19, 2026" />
          </div>
          <div>
            <label for="who">Who</label>
            <input id="who" type="text" value="Students interested in FLL Challenge" />
          </div>
        </div>

        <div class="form-grid two">
          <div>
            <label for="capacity">Capacity</label>
            <input id="capacity" type="text" value="12–16 students" />
          </div>
          <div>
            <label for="coaching">Coaching</label>
            <input id="coaching" type="text" value="Led by our FTC team with adult supervision" />
          </div>
        </div>

        <div class="form-grid two">
          <div>
            <label for="showcase">Showcase / Final Event</label>
            <input id="showcase" type="text" value="Friday mock competition and presentations" />
          </div>
          <div>
            <label for="learn_more_url">Learn More URL</label>
            <input id="learn_more_url" type="text" value="https://www.firstinspires.org/robotics/fll" />
          </div>
        </div>

        <div class="form-grid">
          <div>
            <label for="what_it_is">What It Is</label>
            <textarea id="what_it_is">Students learn robot building, programming, mission strategy, innovation project skills, presentation skills, and teamwork through a complete FIRST LEGO League Challenge camp experience. Our FTC team will teach and guide students throughout the week.</textarea>
          </div>
        </div>

        <div class="form-grid">
          <div>
            <label for="support_text">Support / Fundraising Text</label>
            <textarea id="support_text">All funds from sign-ups will go directly to supporting FTC Team 26502, BRB Robotics.</textarea>
          </div>
        </div>

        <div class="button-row">
          <button class="primary" id="generateBtn">Generate Markdown</button>
          <button class="secondary" id="copyBtn">Copy Markdown</button>
          <button class="success" id="downloadBtn">Download .md File</button>
        </div>

        <p class="small" id="statusText"></p>
      </div>

      <div class="card">
        <div class="pill">Generated Output</div>
        <h2 class="section-title">Markdown Preview</h2>
        <div id="preview" class="preview"></div>
      </div>
    </div>
  </div>

  <script>
    function escapeQuotes(str) {
      return String(str || "").replace(/"/g, '\\"').trim();
    }

    function getValue(id) {
      return document.getElementById(id).value;
    }

    function buildDateTimeWithOffset() {
      const dt = getValue("date").trim();
      const tz = getValue("timezone").trim() || "-05:00";
      if (!dt) return "";
      return dt + ":00" + tz;
    }

    function buildEventDatesYaml() {
      const raw = getValue("event_dates").trim();
      if (!raw) return "";
      const dates = raw.split(",").map(d => d.trim()).filter(Boolean);
      if (!dates.length) return "";
      return dates.map(d => `- ${d}`).join("\n");
    }

    function generateMarkdown() {
      const title = escapeQuotes(getValue("title"));
      const date = buildDateTimeWithOffset();
      const shortDescription = escapeQuotes(getValue("short_description"));
      const pageHeaderImage = escapeQuotes(getValue("page_header_image"));
      const description = escapeQuotes(getValue("description"));
      const stripeUrl = getValue("stripe_url").trim();
      const eventDatesYaml = buildEventDatesYaml();
      const time = escapeQuotes(getValue("time"));
      const location = escapeQuotes(getValue("location"));
      const layout = escapeQuotes(getValue("layout"));
      const draft = getValue("draft").trim();

      const overviewHeading = getValue("overview_heading").trim();
      const theme = getValue("theme").trim();
      const whenText = getValue("when_text").trim();
      const who = getValue("who").trim();
      const capacity = getValue("capacity").trim();
      const coaching = getValue("coaching").trim();
      const showcase = getValue("showcase").trim();
      const whatItIs = getValue("what_it_is").trim();
      const learnMoreUrl = getValue("learn_more_url").trim();
      const supportText = getValue("support_text").trim();

      const markdown = `---
title: "${title}"
date: ${date}
short_description: "${shortDescription}"
page_header_image: "${pageHeaderImage}"
description: "${description}"

stripe_url: ${stripeUrl}
event_dates:
${eventDatesYaml}

time: "${time}"
location: "${location}"
layout: "${layout}"
draft: ${draft}
---

<h1>${overviewHeading}</h1>

<div>
  <strong>Theme:</strong> ${theme}
</div>

<div>
  <strong>When:</strong> ${whenText}
</div>

<div>
  <strong>Time:</strong> ${time}
</div>

<div>
  <strong>Where:</strong> ${location}
</div>

<div>
  <strong>Who:</strong> ${who}
</div>

<div>
  <strong>Capacity:</strong> ${capacity}
</div>

<div>
  <strong>Coaching:</strong> ${coaching}
</div>

<div>
  <strong>Showcase:</strong> ${showcase}
</div>

</br>

<h1>What It Is</h1>

<div>
  ${whatItIs}
</div>

</br>

<h1>More Info</h1>

<div>
  <a href="${learnMoreUrl}"
   target="_blank"
   rel="noopener"
   aria-label="Learn more about FIRST LEGO League"
   style="color: white; background-color: #00193e; padding: 10px 20px; text-decoration: none; border-radius: 6px; display: inline-block; font-weight: 600;">
  Learn More: FIRST LEGO League
</a>  
</div>

</br>

<div>
  <h5>${supportText}</h5>
</div>
`;
      return markdown;
    }

    function updatePreview() {
      const output = generateMarkdown();
      document.getElementById("preview").textContent = output;
      return output;
    }

    async function copyMarkdown() {
      const output = updatePreview();
      const status = document.getElementById("statusText");
      try {
        await navigator.clipboard.writeText(output);
        status.textContent = "Markdown copied to clipboard.";
      } catch (err) {
        status.textContent = "Clipboard copy may not work in some sandboxed environments. You can still download the file.";
      }
    }

    function downloadMarkdown() {
      const output = updatePreview();
      const filename = getValue("filename").trim() || "event-page.md";
      const blob = new Blob([output], { type: "text/markdown;charset=utf-8" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      a.remove();
      URL.revokeObjectURL(url);

      document.getElementById("statusText").textContent = `Downloaded ${filename}`;
    }

    document.getElementById("generateBtn").addEventListener("click", updatePreview);
    document.getElementById("copyBtn").addEventListener("click", copyMarkdown);
    document.getElementById("downloadBtn").addEventListener("click", downloadMarkdown);

    updatePreview();
  </script>
</body>
</html>