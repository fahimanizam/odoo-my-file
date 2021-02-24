# See LICENSE file for full copyright and licensing details.

{
    "name": "Evaluation Management for Education ERP",
    "version": "14.0.1.0.0",
    "author": "Serpent Consulting Services Pvt. Ltd.",
    "website": "http://www.almisnadtechnology.com",
    "category": "School Management",
    "license": "AGPL-3",
    "complexity": "easy",
    "summary": "A Module For Evaluation Management In School",
    "images": ["static/description/Evaluation1.jpg"],
    "depends": ["school", "rating", "exam"],
    "data": [
        "security/evaluation_security.xml",
        "security/ir.model.access.csv",
        "views/school_evaluation_view.xml",
        "views/templates.xml",
        "reports/student_report.xml",
        "reports/student_evaluation.xml"
    ],
    "demo": ["demo/school_evaluation_demo.xml"],
    "installable": True,
    "application": True,
}
