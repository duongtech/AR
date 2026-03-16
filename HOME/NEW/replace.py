import sys

file_path = r'c:\Users\NgocDuong\Downloads\NEW\AR\HOME\NEW\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Locate the start and end of the on-tap section
start_marker = '<!-- ======= ÔN TẬP CHỦ ĐỀ SECTION ======= -->'
end_marker = '</section>'
start_idx = content.find(start_marker)

if start_idx == -1:
    print('Start marker not found')
    sys.exit(1)

# Find the end of the section by looking for the next </section> after the start marker
end_idx = content.find(end_marker, start_idx) + len(end_marker)

if end_idx < len(end_marker):
    print('End marker not found')
    sys.exit(1)

new_content = '''<!-- ======= ÔN TẬP CHỦ ĐỀ SECTION ======= -->
		<section id="on-tap" style="display:none;padding:0 0 2em;">
			<style>
				/* ── Ôn tập: AR topic card grid ── */
				.ontap-hero {
					text-align: center;
					padding: 2.2em 1.5em 1.2em;
					border-bottom: 1px solid rgba(0,0,0,.07);
				}
				.ontap-hero h2 { margin-bottom: .25em; color: #0f3460; font-size: 1.6em; font-weight: 800; }
				.ontap-hero p { opacity: .68; font-size: .96em; margin: 0; }
				.ontap-grid {
					display: grid;
					grid-template-columns: repeat(2, 1fr);
					gap: 1.6em;
					max-width: 900px;
					margin: 1.8em auto 0;
					padding: 0 1.5em 2.2em;
				}
				@media (max-width: 700px) {
					.ontap-grid { grid-template-columns: 1fr; }
				}
				.ontap-card {
					background: #fff;
					border-radius: 18px;
					overflow: hidden;
					box-shadow: 0 4px 22px rgba(0,0,0,.1);
					display: flex;
					flex-direction: column;
					transition: transform .32s cubic-bezier(.25,.8,.25,1), box-shadow .32s ease;
					position: relative;
				}
				.ontap-card::before {
					content: '';
					position: absolute;
					top: 0; left: 0; right: 0;
					height: 4px;
					background: linear-gradient(90deg, #f5c842, #ff8c00, #f5c842);
					background-size: 200%;
					animation: card-top-shimmer 3s linear infinite;
				}
				.ontap-card:hover {
					transform: translateY(-8px) scale(1.01);
					box-shadow: 0 22px 52px rgba(0,0,0,.16);
				}
				.ontap-card-img {
					width: 100%;
					height: 170px;
					object-fit: cover;
					display: block;
				}
				.ontap-card-body {
					padding: 1.2em 1.4em 1.4em;
					display: flex;
					flex-direction: column;
					flex: 1;
				}
				.ontap-card-badge {
					display: inline-block;
					background: rgba(15,52,96,.09);
					color: #0f3460;
					font-size: .68em;
					font-weight: 700;
					letter-spacing: 1.2px;
					text-transform: uppercase;
					border-radius: 4px;
					padding: 3px 10px;
					margin-bottom: .6em;
				}
				.ontap-card-title {
					font-size: 1em;
					font-weight: 800;
					color: #0f3460;
					margin: 0 0 .5em;
					letter-spacing: .03em;
					line-height: 1.35;
				}
				.ontap-card-desc {
					font-size: .88em;
					color: #556;
					line-height: 1.72;
					flex: 1;
					margin: 0 0 1em;
				}
				.ontap-card-actions {
					display: flex;
					gap: .7em;
					flex-wrap: wrap;
					align-items: center;
					margin-top: auto;
				}
				.ontap-btn-primary {
					background: linear-gradient(135deg, #0f3460, #1a5276);
					color: #fff !important;
					border: none !important;
					padding: .6em 1.4em;
					border-radius: 8px;
					font-size: .85em;
					font-weight: 700;
					cursor: pointer;
					text-decoration: none;
					display: inline-block;
					transition: transform .2s, box-shadow .2s;
					box-shadow: 0 3px 12px rgba(15,52,96,.3);
				}
				.ontap-btn-primary:hover {
					transform: translateY(-2px);
					box-shadow: 0 6px 20px rgba(15,52,96,.4);
					color: #fff !important;
				}
				.ontap-btn-quiz {
					background: transparent;
					color: #0f3460 !important;
					border: 1.5px solid rgba(15,52,96,.3) !important;
					padding: .55em 1.1em;
					border-radius: 8px;
					font-size: .82em;
					font-weight: 600;
					cursor: pointer;
					text-decoration: none;
					display: inline-block;
					transition: background .2s, border-color .2s;
				}
				.ontap-btn-quiz:hover {
					background: rgba(15,52,96,.07);
					border-color: rgba(15,52,96,.6) !important;
				}
				/* Divider before quiz area */
				.ontap-quiz-divider {
					text-align: center;
					padding: 2em 1.5em 1em;
					border-top: 1px solid rgba(0,0,0,.08);
					background: #f7f9ff;
				}
				.ontap-quiz-divider h3 {
					color: #0f3460;
					font-size: 1.2em;
					font-weight: 800;
					margin-bottom: .25em;
				}
				.ontap-quiz-divider p { opacity: .65; font-size: .9em; margin: 0 0 1.2em; }

				/* Topic group tabs in quiz area */
				.ontap-topic-tabs {
					display: flex;
					flex-wrap: wrap;
					gap: .6em;
					justify-content: center;
					margin-bottom: 1.4em;
				}
				.ontap-tab-group {
					display: flex;
					flex-direction: column;
					align-items: center;
					gap: .4em;
				}
				.ontap-sub-tabs {
					display: none;
					flex-wrap: wrap;
					gap: .45em;
					justify-content: center;
					padding: .4em .7em;
					background: #f5f5f5;
					border: 1px solid #ddd;
					border-radius: 8px;
				}
				.ontap-sub-tabs.open { display: flex; }
			</style>

			<article class="post featured" style="padding: 0;">

				<!-- Hero header -->
				<div class="ontap-hero">
					<h2>🌟 Ôn Tập Chủ Đề</h2>
					<p>Chọn chủ đề để xem bài học tương tác hoặc làm bài ôn tập</p>
				</div>

				<!-- 4 AR topic cards -->
				<div class="ontap-grid">

					<!-- AR1: Xác định phương hướng -->
					<div class="ontap-card">
						<img class="ontap-card-img" src="images/ar1.jpg" alt="Xác định các phương trong không gian"
							onerror="this.style.background='linear-gradient(135deg,#0f3460,#16213e)';this.style.height='170px';this.alt='';this.src=''">
						<div class="ontap-card-body">
							<span class="ontap-card-badge">Thiên văn học</span>
							<h3 class="ontap-card-title">Xác Định Các Phương Trong Không Gian</h3>
							<p class="ontap-card-desc">Mô phỏng quỹ đạo Mặt Trời theo mùa trong năm. Quan sát góc cao, bóng nắng, pha ngày đêm theo thời gian thực bằng đồ hoạ 3D tương tác.</p>
							<div class="ontap-card-actions">
								<a href="../../AR1/index.html" class="ontap-btn-primary">Vào học →</a>
								<button class="ontap-btn-quiz ripple-btn" onclick="startOntapQuizGroup('phuong-huong')">📋 Ôn tập</button>
							</div>
						</div>
					</div>

					<!-- AR2: Mặt Trời – Trái Đất – Mặt Trăng -->
					<div class="ontap-card">
						<img class="ontap-card-img" src="images/ar2.jpg" alt="Mặt Trời, Trái Đất, Mặt Trăng"
							onerror="this.style.background='linear-gradient(135deg,#0f3460,#16213e)';this.style.height='170px';this.alt='';this.src=''">
						<div class="ontap-card-body">
							<span class="ontap-card-badge">Thiên văn học</span>
							<h3 class="ontap-card-title">Mặt Trời, Trái Đất, Mặt Trăng</h3>
							<p class="ontap-card-desc">Mô phỏng 8 hành tinh quỹ đạo quanh Mặt Trời với tốc độ, khoảng cách và tỉ lệ thực tế trong không gian 3D — xoay, zoom tự do.</p>
							<div class="ontap-card-actions">
								<a href="../../AR2/index.html" class="ontap-btn-primary">Vào học →</a>
								<button class="ontap-btn-quiz ripple-btn" onclick="startOntapQuizGroup('mat-troi')">📋 Ôn tập</button>
							</div>
						</div>
					</div>

					<!-- AR3: Bề mặt Trái Đất -->
					<div class="ontap-card">
						<img class="ontap-card-img" src="images/ar3.jpg" alt="Bề mặt Trái Đất"
							onerror="this.style.background='linear-gradient(135deg,#0f3460,#16213e)';this.style.height='170px';this.alt='';this.src=''">
						<div class="ontap-card-body">
							<span class="ontap-card-badge">Địa lý học</span>
							<h3 class="ontap-card-title">Bề Mặt Trái Đất</h3>
							<p class="ontap-card-desc">Trò chơi kéo thả nhận dạng châu lục, đại dương trên bản đồ thế giới tương tác. Học bằng cách chơi — phản hồi tức thì sau mỗi câu trả lời.</p>
							<div class="ontap-card-actions">
								<a href="../../AR3/index.html" class="ontap-btn-primary">Vào học →</a>
								<button class="ontap-btn-quiz ripple-btn" onclick="startOntapQuizGroup('be-mat')">📋 Ôn tập</button>
							</div>
						</div>
					</div>

					<!-- AR4: Đới khí hậu -->
					<div class="ontap-card">
						<img class="ontap-card-img" src="images/ar4.jpg" alt="Trái Đất và các đới khí hậu"
							onerror="this.style.background='linear-gradient(135deg,#0f3460,#16213e)';this.style.height='170px';this.alt='';this.src=''">
						<div class="ontap-card-body">
							<span class="ontap-card-badge">Địa lý học</span>
							<h3 class="ontap-card-title">Trái Đất Và Các Đới Khí Hậu</h3>
							<p class="ontap-card-desc">Phân bố 5 đới khí hậu trên Địa Cầu 3D tương tác. Tích hợp hệ thống câu hỏi kiểm tra kiến thức và mini-game học tập.</p>
							<div class="ontap-card-actions">
								<a href="../../AR4/index.html" class="ontap-btn-primary">Vào học →</a>
								<button class="ontap-btn-quiz ripple-btn" onclick="startOntapQuizGroup('khi-hau')">📋 Ôn tập</button>
							</div>
						</div>
					</div>

				</div><!-- /ontap-grid -->

				<!-- Quiz area divider -->
				<div class="ontap-quiz-divider" id="ontap-quiz-section" style="display:none;">
					<h3>📝 Bộ Đề Ôn Tập Theo Chủ Đề</h3>
					<p>Chọn bộ đề để bắt đầu ôn tập</p>

					<!-- Tabs: tổng hợp -->
					<div class="ontap-topic-tabs" id="quiz-tabs-on-tap">
						<!-- Nhóm tổng hợp -->
						<div class="ontap-tab-group">
							<button onclick="toggleSubMenuNew('sub-tong-hop')" class="button" style="font-size:.82em;">🌏 Ôn tập tổng hợp ▾</button>
							<div class="ontap-sub-tabs" id="sub-tong-hop">
								<button onclick="startQuiz(0, 'on-tap')" class="button" style="font-size:.78em;background:#fff;">📋 Đề 1</button>
								<button onclick="startQuiz(1, 'on-tap')" class="button" style="font-size:.78em;background:#fff;">📋 Đề 2</button>
							</div>
						</div>
						<!-- Nhóm phương hướng -->
						<div class="ontap-tab-group" id="ontap-group-phuong-huong">
							<button onclick="toggleSubMenuNew('sub-phuong-huong')" class="button" style="font-size:.82em;">🧭 Xác định phương hướng ▾</button>
							<div class="ontap-sub-tabs" id="sub-phuong-huong">
								<button onclick="startQuiz(2, 'on-tap')" class="button" style="font-size:.78em;background:#fff;">📋 Bộ đề 1</button>
							</div>
						</div>
						<!-- Nhóm Mặt Trời -->
						<div class="ontap-tab-group" id="ontap-group-mat-troi">
							<button onclick="toggleSubMenuNew('sub-mat-troi')" class="button" style="font-size:.82em;">☀️ Mặt Trời – Trái Đất ▾</button>
							<div class="ontap-sub-tabs" id="sub-mat-troi">
								<button onclick="startQuiz(5, 'on-tap')" class="button" style="font-size:.78em;background:#fff;">📋 Bộ đề 1</button>
							</div>
						</div>
						<!-- Nhóm Bề mặt -->
						<div class="ontap-tab-group" id="ontap-group-be-mat">
							<button onclick="toggleSubMenuNew('sub-be-mat')" class="button" style="font-size:.82em;">🌍 Bề mặt Trái Đất ▾</button>
							<div class="ontap-sub-tabs" id="sub-be-mat">
								<button onclick="startQuiz(4, 'on-tap')" class="button" style="font-size:.78em;background:#fff;">📋 Bộ đề 1</button>
							</div>
						</div>
						<!-- Nhóm khí hậu -->
						<div class="ontap-tab-group" id="ontap-group-khi-hau">
							<button onclick="toggleSubMenuNew('sub-khi-hau')" class="button" style="font-size:.82em;">🌡️ Đới khí hậu ▾</button>
							<div class="ontap-sub-tabs" id="sub-khi-hau">
								<button onclick="startQuiz(3, 'on-tap')" class="button" style="font-size:.78em;background:#fff;">📋 Bộ đề 1</button>
							</div>
						</div>
					</div>

					<!-- Khu vực làm bài -->
					<div id="quiz-area-on-tap" style="display:none;max-width:760px;margin:0 auto;text-align:left;">
						<div id="quiz-header-on-tap"
							style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1em;">
							<span id="quiz-title-on-tap" style="font-weight:700;font-size:1.05em;"></span>
							<span id="quiz-progress-on-tap" style="opacity:.6;font-size:.88em;"></span>
						</div>
						<div id="quiz-question-on-tap"
							style="font-size:1em;font-weight:600;margin-bottom:1em;line-height:1.6;"></div>
						<div id="quiz-choices-on-tap" style="display:grid;gap:.6em;"></div>
						<div id="quiz-feedback-on-tap"
							style="margin-top:.9em;padding:.7em 1em;border-radius:8px;display:none;font-size:.93em;">
						</div>
						<div style="margin-top:1.2em;display:flex;gap:.8em;flex-wrap:wrap;">
							<button id="quiz-next-on-tap" onclick="quizNext()" class="button" style="display:none;">Câu
								tiếp theo ➡️</button>
							<button onclick="backToTopics()" class="button"
								style="background:transparent;color:inherit;border-color:rgba(0,0,0,.3);font-size:.82em;">↩
								Đóng</button>
						</div>
						<div id="quiz-result-on-tap" style="display:none;text-align:center;padding:1.5em;"></div>
					</div>
				</div><!-- /ontap-quiz-divider -->

			</article>

			<script>
				// Open a named sub-menu in the Ôn tập quiz section
				function toggleSubMenuNew(id) {
					var el = document.getElementById(id);
					if (!el) return;
					// Toggle logical
					var isOp = el.classList.contains('open');
					// Close all first to keep it clean
					['sub-tong-hop','sub-phuong-huong','sub-mat-troi','sub-be-mat','sub-khi-hau'].forEach(function(s) {
						var sel = document.getElementById(s);
						if (sel) sel.classList.remove('open');
					});
					if (!isOp) {
						el.classList.add('open');
					}
				}

				// Called from the card "Ôn tập" buttons — reveals the quiz section and opens that group
				function startOntapQuizGroup(group) {
					var sec = document.getElementById('ontap-quiz-section');
					if (sec) {
						sec.style.display = '';
						// Smooth scroll to quiz section
						setTimeout(function() {
							sec.scrollIntoView({ behavior: 'smooth', block: 'start' });
						}, 80);
					}
					// Map group → sub menu id
					var map = {
						'phuong-huong': 'sub-phuong-huong',
						'mat-troi': 'sub-mat-troi',
						'be-mat': 'sub-be-mat',
						'khi-hau': 'sub-khi-hau'
					};
					var subId = map[group];
					if (subId) {
						// Open the specific section
						toggleSubMenuNew(subId);
					}
				}
			</script>
		</section>'''

modified_content = content[:start_idx] + new_content + content[end_idx:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(modified_content)

print('Successfully replaced on-tap section')
