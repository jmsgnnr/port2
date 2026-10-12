from reportlab.platypus import SimpleDocTemplate,Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from xml.sax.saxutils import escape
p=r'C:\Users\james\Development\port2\assets\James_Potee_Resume.pdf'
navy=HexColor('#17283a'); gray=HexColor('#475569')
styles={
'name':ParagraphStyle('name',fontName='Helvetica-Bold',fontSize=17.5,leading=20.5,textColor=navy,spaceAfter=2),
'contact':ParagraphStyle('contact',fontName='Helvetica',fontSize=8.7,leading=11.5,textColor=gray,spaceAfter=8),
'section':ParagraphStyle('section',fontName='Helvetica-Bold',fontSize=10.5,leading=14,textColor=navy,spaceBefore=8,spaceAfter=4),
'job':ParagraphStyle('job',fontName='Helvetica-Bold',fontSize=10,leading=14,textColor=navy,spaceBefore=5,spaceAfter=1),
'body':ParagraphStyle('body',fontName='Helvetica',fontSize=9,leading=13,spaceAfter=4),
'bullet':ParagraphStyle('bullet',fontName='Helvetica',fontSize=8.8,leading=12.5,leftIndent=12,firstLineIndent=-8,spaceAfter=3),
}
doc=SimpleDocTemplate(p,pagesize=letter,rightMargin=45,leftMargin=45,topMargin=27,bottomMargin=34,title='James G. Potee | Resume',author='James G. Potee')
story=[]
def add(style,t):story.append(Paragraph(t,styles[style]))
def sec(t):add('section',t.upper())
def job(title,period,org):add('job',f'{escape(title)} <font color="#64748b">| {escape(period)}</font>');add('body',escape(org))
def bullets(items):
 for x in items:add('bullet','&#8226; '+escape(x))
add('name','JAMES G. POTEE')
add('contact','+1 (720) 693-3007  |  jamespotee@gmail.com  |  github.com/jmsgnnr')
add('body','Cloud infrastructure, platforms, security and networking engineer with experience building AWS governance platforms, identity automation, and resilient enterprise infrastructure.')
sec('Experience')
job('Systems Engineer IV - AWS Cloud Infrastructure','2023 - Current','Charter Communications / The Select Group (Contract) | Remote')
bullets(['Primary frontend contributor to a production internal AWS management platform, building Next.js/React and TypeScript experiences for account administration, IP address management, role-based access, and identity assignments.','Engineered cross-account IAM access-key monitoring using AWS Config, STS, Lambda, DynamoDB, SES and scheduled automation.','Built Python tooling and Django/React interfaces for AWS Identity Center self-service, bulk user/group operations, permission assignments and account access.','Worked across AWS networking, VPCs, Transit Gateways, Route 53, EKS, infrastructure automation and security governance; collaborated with infrastructure and security stakeholders.','Supported Terraform, CloudFormation and GitLab CI/CD workflows for repeatable platform and infrastructure changes.'])
job('Senior Data Analyst','2022','Sagence Inc. (Contract) | Chicago, IL')
bullets(['Developed SQL and Oracle Data Integrator (ODI) transformation pipelines to consolidate legacy data for enterprise reporting.','Supported data warehouse design, AWS-hosted data migrations and requirements translation for business stakeholders.'])
job('Web Developer I','2021–2022','On Beat Digital | Fort Collins, CO')
bullets(['Built responsive web applications and marketing/analytics interfaces.','Developed AWS Lambda and S3 workflows and Python integrations for processing external API data into operational reports.'])
sec('Selected Platform & Automation Work')
bullets(['Internal AWS management platform: Next.js, React, TypeScript, AWS SDK, identity federation and governance workflows.','Cloud security automation: IAM access-key monitoring, AWS account discovery, cross-account access and notifications.','Identity self-service: AWS Identity Center, Python, Django/React, validation and dry-run safeguards.'])
sec('Technical Skills')
for k,v in [('Infrastructure & networking','AWS, EC2, EKS, VPC, Transit Gateway, VPC peering, Route 53, RDS, CIDR, routing, DNS'),('Security & identity','IAM, Identity Center, AWS Organizations, AWS Config, CloudTrail, KMS, RBAC, SSO, Keycloak, access governance'),('Automation & delivery','Python, boto3, PowerShell, Terraform, CloudFormation, GitLab CI/CD, Docker, Kubernetes, Helm'),('Development & data','React, Next.js, TypeScript, REST APIs, SQL, PostgreSQL, DynamoDB'),('Observability','CloudWatch, Datadog, centralized logging')]:
 add('body',f'<b>{escape(k)}:</b> {escape(v)}')
sec('Education')
add('body','<b>Software Engineering Immersive</b> | General Assembly | 2020–2021 | Top of Class Honors')
sec('Community')
add('body','STEM Mentor | Latinos In Tech Early Career Development Program | 2023–Present')
doc.build(story)
print('RESUME_CREATED',p)
