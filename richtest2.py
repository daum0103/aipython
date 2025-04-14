from rich.console import Console
from rich.table import Table
from rich.progress import track
import time

console = Console()

# 1. 컬러 텍스트 출력
console.print("[bold magenta]Hello, Rich![/bold magenta] :sparkles:")

# 2. 테이블 출력
table = Table(title="우리집 구성원 정보")

table.add_column("이름", justify="left", style="cyan", no_wrap=True)
table.add_column("나이", style="green")
table.add_column("직업", justify="right", style="yellow")

table.add_row("다움", "22", "학생")
table.add_row("사랑이", "13", "이쁘니")
table.add_row("행운이", "8", "홈프로텍터")

console.print(table)

# 3. 프로그레스 바 출력
for task in track(range(10), description="처리 중..."):
    time.sleep(0.1)



from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout
from rich.text import Text
from rich.align import Align

console = Console()

# 전체 레이아웃 구성
layout = Layout()

layout.split(
    Layout(name="header", size=3),
    Layout(name="body", ratio=1),
    Layout(name="footer", size=3),
)

layout["body"].split_row(
    Layout(name="sidebar", size=30),
    Layout(name="main", ratio=1)
)

# 헤더
layout["header"].update(
    Panel(
        Align.center("[bold magenta]★ 다움의 미니홈피에 오신 걸 환영합니다 ★", vertical="middle"),
        style="bold white on dark_green"
    )
)

# 사이드바 - 프로필
profile = Table.grid(padding=1)
profile.add_column(justify="center")
profile.add_row("[bold cyan]🌈 다움움's Profile")
profile.add_row("📸 [italic]사진은 준비 중...[/italic]")
profile.add_row("📍 부산")
profile.add_row("💬 상태메시지: [bold yellow]요즘 범고래 사냥하기에 빠짐[/bold yellow]")

layout["sidebar"].update(Panel(profile, title="👤 프로필", border_style="cyan"))

# 메인 - 방명록 or 게시글
guestbook = Table.grid(padding=1)
guestbook.add_column()
guestbook.add_row("[bold green]📝 최근 게시글")
guestbook.add_row("- 오늘 rich로 미니홈피 만들었다. 신기방기!")
guestbook.add_row("- 지피띠니 진짜 뭐든 다 되네...😮")
guestbook.add_row("- 누가 방명록 좀 남겨줘요ㅠㅠ")

layout["main"].update(Panel(guestbook, title="📒 게시판", border_style="green"))

# 푸터
footer_text = Text("ⓒ 2025. 다움움's Console Minihomepy | 방명록은 언제나 환영 😊", style="dim")
layout["footer"].update(Align.center(footer_text, vertical="middle"))

# 출력
console.print(layout)